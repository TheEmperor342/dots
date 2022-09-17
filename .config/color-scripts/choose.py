import random, os, subprocess

dirs = os.listdir("/home/emperor/.config/color-scripts/")
dirs.remove("choose.py")

os.system("$HOME/.config/color-scripts/"+random.choice(dirs))

