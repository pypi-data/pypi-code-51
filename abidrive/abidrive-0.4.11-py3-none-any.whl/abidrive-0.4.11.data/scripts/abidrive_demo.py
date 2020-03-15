#!python
"""
Example usage of the AbiDrive python library to monitor and control AbiDrive devices
"""

from __future__ import print_function

import abidrive
from abidrive.enums import *
import time
import math

# Find a connected AbiDrive (this will block until you connect one)
print("finding an abidrive...")
my_drive = abidrive.find_any()

# Find an AbiDrive that is connected on the serial port /dev/ttyUSB0
#my_drive = abidrive.find_any("serial:/dev/ttyUSB0")

# Calibrate motor and wait for it to finish
print("starting calibration...")
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while my_drive.axis0.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# To read a value, simply read the property
print("Bus voltage is " + str(my_drive.vbus_voltage) + "V")

# Or to change a value, just assign to the property
my_drive.axis0.controller.pos_setpoint = 3.14
print("Position setpoint is " + str(my_drive.axis0.controller.pos_setpoint))

# And this is how function calls are done:
for i in [1,2,3,4]:
    print('voltage on GPIO{} is {} Volt'.format(i, my_drive.get_adc_voltage(i)))

# A sine wave to test
t0 = time.monotonic()
while True:
    setpoint = 10000.0 * math.sin((time.monotonic() - t0)*2)
    print("goto " + str(int(setpoint)))
    my_drive.axis0.controller.pos_setpoint = setpoint
    time.sleep(0.01)

# Some more things you can try:

# Write to a read-only property:
my_drive.vbus_voltage = 11.0  # fails with `AttributeError: can't set attribute`

# Assign an incompatible value:
my_drive.motor0.pos_setpoint = "I like trains"  # fails with `ValueError: could not convert string to float`
