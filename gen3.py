import serial
import pycrc
import time

try:
    s = serial.Serial("/dev/ttyUSB0", 9600)

    cmd = [0, 0, 0, 0, 0, 0, 0, 0]


# except Exception as e:
#     print("Port not found")
#

    def relay_on(relay_ch):
        cmd[0] = 0x01
        cmd[1] = 0x05
        cmd[2] = 0x00
        cmd[3] = relay_ch - 1
        cmd[4] = 0xff
        cmd[5] = 0x00
        crc = pycrc.ModbusCRC(cmd[0:6])
        cmd[6] = crc & 0xff
        cmd[7] = crc >> 8


    def relay_off(relay_ch):
        cmd[0] = 0x01
        cmd[1] = 0x05
        cmd[2] = 0x00
        cmd[3] = relay_ch - 1
        cmd[4] = 0x00
        cmd[5] = 0x00
        crc = pycrc.ModbusCRC(cmd[0:6])
        cmd[6] = crc & 0xff
        cmd[7] = crc >> 8


    while True:

            genset = 0
            push_btn = 0

            relay_off(1)

            relay_on(2)
            relay_on(3)
            relay_on(6)
            relay_on(7)

            relay_off(4)
            relay_on(5)

            if genset == 1:
                relay_on(1)


            elif push_btn == 1:
                relay_on(4)
                relay_off(5)

            s.write(bytes(cmd))
            time.sleep(0.2)

except Exception as e:
    print("Port not found")
