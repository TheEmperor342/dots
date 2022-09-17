#!/usr/bin/env bash

PICTURE=/tmp/lock.png
SCREENSHOT="scrot $PICTURE"

BLUR="5x4"

$SCREENSHOT
convert $PICTURE -blur $BLUR $PICTURE
betterlockscreen -u $PICTURE -l
rm $PICTURE
