#!/usr/bin/env python3
########################################################################
# Filename    : INA219.py
# Description : I2C Power Monitor
# Author      : Nimble Hub LLC
# modification: 2019/3/24
########################################################################

from ina219 import INA219
from ina219 import DeviceRangeError
#from time import sleep
SHUNT_OHMS = 0.1
#MAX_EXPECTED_AMPS = 2.0
#ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
#ina.configure(ina.RANGE_16V)
def read_ina219():
        ina = INA219(SHUNT_OHMS)
        ina.configure()
        print " Bus Voltage: %.3f V" % ina.voltage()
        try:
            print " Bus Current: %.3f mA" % ina.current()
            print " Power: %.3f mW" % ina.power()
            print " Shunt Voltage: %.3f mV" % ina.shunt_voltage()
        except DeviceRangeError as e:
            print(e)
if __name__ == "__main__":
    read_ina219()

            