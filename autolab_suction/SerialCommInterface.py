"""
Low level communication between Python and Arduino via pySerial.
Arthor: Jason Liu <xinyuliu@berkeley.edu>
"""

from serial import Serial
from multiprocessing import Process, Queue

import time

VACUUM_WARM_UP_TIME = 3 # time for the vacuum to warm up, in seconds

class _VacuumSerial(Process):
    """ Private class that abstracts continuous serial communication with Arduino board.
    """
    def __init__(self, flags_q, vacuum_comm, baudrate):
        Process.__init__(self)
        
        self._vacuum_comm = vacuum_comm
        self._baudrate = baudrate
        self._flags_q = flags_q
        self._flags = {
            "stopping" : False,
            "suction" : False,
        }

        # IPython.embed()

    def run(self):
        self.ser = Serial(port=self._vacuum_comm, baudrate=self._baudrate)
        self._stop_robot()
        time.sleep(VACUUM_WARM_UP_TIME)

        while True:
            if not self._flags_q.empty():
                flag = self._flags_q.get();
                self._flags[flag[0]] = flag[1]

            if self._flags["stopping"]:
                self._flags_q.close()
                self.ser.close()
                break

            if self._flags["suction"]:
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()
                self.ser.write("v")

            if not self._flags["suction"]:
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()
                self.ser.write("x")

    def _sendControls(self, requests):
        self.ser.reset_output_buffer()
        PWMs = []
        for req in requests:
            if req >= 0:
                PWMs.append(int(req))
                PWMs.append(0)
            else:
                PWMs.append(0)
                PWMs.append(int(abs(req)))
        for e in PWMs:
            self.ser.write(chr(e))
            
    def _control(self, requests):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write("s")
        self._sendControls(requests)
        
    def _stop_robot(self):
        self._control([0,0,0,0,0,0])

class VacuumSerialInterface:
    
    def __init__(self, vacuum_comm, baudrate):
        self._comm = vacuum_comm
        self._baudrate = baudrate
        self._reset()

    def _reset(self):
        self._flags_q = Queue()
        self._dex_serial = _VacuumSerial(self._flags_q, self._comm, self._baudrate)

    def start(self):
        self._dex_serial.start()
        time.sleep(VACUUM_WARM_UP_TIME)
        
    def stop(self):
        self._flags_q.put(("stopping", True))
        self._reset()

    def on(self):
        self._flags_q.put(("suction", True))
        
    def off(self):
        self._flags_q.put(("suction", False))
