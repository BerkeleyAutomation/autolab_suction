"""
Python-Bluetooth Interface for the Vacuum Hand Project
Author: Albert Li <alberthli@berkeley.edu>
"""
import serial
import time

# Initializing the serial connection. The port name should be changed with every computer.
baudrate = 57600
port = '/dev/cu.VacuumHand-DevB' # Mac

class VacuumServo:
	def __init__(self):
                self._serialConnection = serial.Serial(port, baudrate, timeout = 1)

	# Sends a command to move the servo to any position between -90 and 90 degrees, inclusive
	def move(self, angle):
		targetAngle = int(angle)

		# Capping angle inputs
		try:
			if targetAngle > 90:
				targetAngle = 90
			elif targetAngle < -90:
				targetAngle = -90
			self._serialConnection.write(str(targetAngle).encode())

		except TypeError:
			print("Please input an integer in the range -90 to 90!")

	# Starts the Vacuum Hand
	def start(self):
		try:
			# Reset block
			time.sleep(2)
			self.move(-90)

			print("Enter an integer angle between -90 and 90 degrees. Ctrl+C to terminate.\n")

			while True:
				self.takeInput()

		except KeyboardInterrupt:
			self.move(0)
			print("Hand Control Terminated.\n")

		except TypeError:
			self.takeInput()
 
 	# Processes input to move the hand
	def takeInput(self):
		print("Enter an angle: ")
		num = input()
		self.move(num)

		# Two-way acknowledge
		print("Command Sent!")
		self._serialConnection.readline()
		print("Movement Successful!\n")

# Initializing the hand and starting it
if __name__ == '__main__':
        v = VacuumServo()
        v.start()
