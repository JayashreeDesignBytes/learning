import os
import time
from datetime import datetime

reboot_times = ["07:23:00", "07:24:00"]

with open("rwboot_log.txt", "a") as log_file:
    log_file.write(f"Reboot scheduled at: {reboot_times}\n")

while True:

    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time in reboot_times:
        with open("rwboot_log.txt", "a") as log_file:
            log_file.write(f"Reboot at: {current_time}\n")
        os.system('sudo reboot -h')
        break

    time.sleep(1)
