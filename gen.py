import serial

import pycrc
import time

s = serial.Serial("/dev/ttyUSB0", 9600)
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01  # Device address
cmd[1] = 0x05  # command

# bydefault genset and push button's are off
genset = 0
Push_btn = 0

while True:
    cmd[2] = 0

    # Valve 2,3 6 & 7 are continuously on
    cmd[3] = 0x02
    cmd[4] = 0xff

    cmd[3] = 0x03
    cmd[4] = 0xff

    cmd[3] = 0x06
    cmd[4] = 0xff

    cmd[3] = 0x07
    cmd[4] = 0xff

    cmd[5] = 0

    crc = pycrc.Modbuscrc(cmd[0:6])
    cmd[6] = crc & 0xFF
    cmd[7] = crc >> 8

    s.write(cmd)
    time.sleep(0.2)

    # when genset is sterted valve 1 is on otherwise off

    if genset == 1:
        cmd[2] = 0,

        cmd[3] == 0x01
        cmd[4] == 0xff

        cmd[5] = 0

        crc = pycrc.Modbuscrc(cmd[0:6])
        cmd[6] = crc & 0xff
        cmd[7] = crc >> 8

        s.write(cmd)
        time.sleep(0.2)

        # push button

    elif Push_btn == 1:
        cmd[2] = 0

        cmd[3] = 0x04
        cmd[4] = 0xff

        cmd[3] = 0x05
        cmd[4] = 0x00

        cmd[5] = 0

        crc = pycrc.Modbuscrc(cmd[0:6])
        cmd[6] = crc & 0xff
        cmd[7] = crc >> 8

        s.write(cmd)
        time.sleep(0.2)

    else:

        cmd[2] = 0

        cmd[3] = 0x04
        cmd[4] = 0x00

        cmd[3] = 0x05
        cmd[4] = 0xff

        cmd[5] = 0

        crc = pycrc.Modbuscrc(cmd[0:6])
        cmd[6] = crc & 0xff
        cmd[7] = crc >> 8

        s.write(cmd)
        time.sleep(0.2)
