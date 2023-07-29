#! /usr/bin/env python3
import sys
import subprocess
import os
import json
with open('config.json') as f:
    config = json.load(f)
useAlbumArt: bool = config['eww']['player']['useAlbumArt']
useAccentColor: bool = config['eww']['player']['useAccentColor']

if sys.argv[1] == '--title':
    print(subprocess.getoutput("playerctl metadata title --player=spotify"))

elif sys.argv[1] == '--artist':
    print('' if (x := subprocess.getoutput(
        "playerctl metadata artist --player=spotify")) == 'No players found' else x)

elif sys.argv[1] == '--status':
    print(subprocess.getoutput("playerctl status --player=spotify"))

elif sys.argv[1] == "--art":
    link = subprocess.getoutput(
        "playerctl metadata mpris:artUrl --player=spotify")

    if link == "No players found" or not useAlbumArt:
        print("images/spotify.svg")

    else:
        linkFsName = link[8:].replace(".", "_").replace("/", "_")
        if linkFsName in os.listdir('albumart'):
            print(f"albumart/{linkFsName}")
        else:
            os.system("cd albumart && ls | grep -xv \".gitkeep\" | xargs rm")
            os.system(f'curl {link} -o albumart/{linkFsName} --silent')
            print(f"albumart/{linkFsName}")

elif sys.argv[1] == "--color":
    isNotPlaying = subprocess.getoutput(
        "playerctl status --player=spotify") == "No players found"
    directory = os.listdir("albumart")
    if isNotPlaying or not useAccentColor:
        print("Nothing playing")
    else:
        colorthief = __import__("colorthief").ColorThief(
            f"albumart/{directory[0]}")
        colors = colorthief.get_color(quality=1)
        print(f"rgba({colors[0]}, {colors[1]}, {colors[2]}, 0.6)")
