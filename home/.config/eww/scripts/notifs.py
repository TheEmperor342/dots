#! /usr/bin/env python3
import subprocess, json

notifsRaw, notifsProcessed = json.loads(subprocess.getoutput("dunstctl history")), []

def genYuck(data: dict) -> str:
  yuck = "(box :orientation \"v\""
  for i, j in data:
    i, j = i.replace("\"", "\\\""), j.replace("\"", "\\\"")
    yuck += f"""(box :orientation "v" :class "container" :space-evenly false :hexpand false
  (label :text "{i}" :limit-width 25)
  (label :text "{j}" :limit-width 25)
)
"""
  return f"{yuck})"
j = 0
for i in notifsRaw['data'][0]:
  if j == 10: break
  notifsProcessed.append((i['summary']['data'], i['body']['data']))
  j += 1

print(genYuck(notifsProcessed))