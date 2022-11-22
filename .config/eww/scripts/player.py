#! /usr/bin/env python3
import sys, subprocess
if sys.argv[1] == '--title':
  print(subprocess.getoutput("playerctl metadata title --player=spotify"))
elif sys.argv[1] == '--artist':
  print('' if (x := subprocess.getoutput("playerctl metadata artist --player=spotify")) == 'No players found' else x)
elif sys.argv[1] == '--status':
  print(subprocess.getoutput("playerctl status --player=spotify"))