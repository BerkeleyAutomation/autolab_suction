"""
Python wrapper for the Arduino vacuum suction control
Author: Jason Liu <xinyuliu@berkeley.edu>
"""
from SerialCommInterface import VacuumSerialInterface
from time import sleep

import logging
import time
import IPython

class Vacuum:
    """
    Abstraction for Arduino vacuum suction. 
    Low level, SerialCommInterface, uses pySerial to communicate with Arduino.
    """

    def __init__(self):
        self._vacuum = VacuumSerialInterface(vacuum_comm="/dev/ttyUSB0", baudrate=115200)
        self._vacuum.start()
    
    def on(self):
        self._vacuum.on()
    
    def off(self):
        self._vacuum.off()

    def stop(self):
        time.sleep(1)
        self._vacuum.stop()
        
def test_vacuum(sleep=10):
    vac = Vacuum()

    print 'suction on'
    vac.on()
    time.sleep(sleep)
    print 'suction off'
    vac.off()
    time.sleep(sleep-2)
    print 'stop robot'
    vac.stop()

if __name__ == '__main__':
    test_vacuum()
