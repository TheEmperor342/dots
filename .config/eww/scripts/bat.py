#!/bin/python3
import subprocess

CHARGE = int(subprocess.check_output("cat /sys/class/power_supply/BAT1/capacity", shell=True).decode())
icon = ''
if CHARGE == 50:
    icon = ' '
elif CHARGE == 100:
    icon = ' '
elif CHARGE < 10:
    icon = ' '
    subprocess.run('notify-send --urgency=critical "10% Charge remaining" "Recharge your device."')
elif CHARGE < 50:
    icon = ' '
elif CHARGE > 50:
    icon = ' '


print(f'{icon} {CHARGE}%')
