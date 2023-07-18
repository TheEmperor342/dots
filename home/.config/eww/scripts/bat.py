#!/usr/bin/env python3
import subprocess

CHARGE = int(subprocess.getoutput("cat /sys/class/power_supply/BAT1/capacity"))
STATUS = subprocess.getoutput("cat /sys/class/power_supply/BAT1/status")
icon = ''
icons = {
    10: ('', ''),
    20: ('', ' '),
    30: ("", ' '),
    40: ('', ' '),
    50: ('', ' '),
    60: ('', ' '),
    70: ('', ' '),
    80: ('', ''),
    90: ('', ''),
    100: ('', ' '),
    110: ('', ' ')
}

for i in range(10, 120, 10):
    if CHARGE == 100:
        if STATUS == "Discharging": icon = icons[110][0]
        elif STATUS == "Full": icon = icons[110][1]
        break
    elif CHARGE <= i:
        if STATUS == "Discharging": icon = icons[i][0]
        elif STATUS == "Charging": icon = icons[i][1]
        break

print(f'{icon} {CHARGE}%')
