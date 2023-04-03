import psutil
import time
from datetime import datetime
import csv
from system_ip import *


def system():
    # Computer name
    computer_name = platform.node()

    # system Local time
    now = datetime.now()
    system_local_time = now.strftime("%H:%M:%S")

    # system uptime
    uptime_used = round((time.time() - psutil.boot_time()), 3)

    # get ip address from ipaddr.py
    my_ip = check_ip()

    # cpu load
    my_cpu_load = psutil.cpu_percent(0.5)

    # Ram Usage
    # Get system memory Usage
    ram = psutil.virtual_memory()

    # Unit function to convert Ram size
    def unit(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    used_ram = unit(ram.used)

    # Write data in csv

    data = [computer_name, system_local_time, uptime_used, my_ip, my_cpu_load, used_ram]

    with open('system_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        # write the header
        # writer.writerow(header)

        # write the data
        writer.writerow(data)
