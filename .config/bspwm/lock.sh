#!/bin/sh

PICTURE=/tmp/lock.png
SCREENSHOT="scrot $PICTURE"

BLUR="5x4"

$SCREENSHOT
convert $PICTURE -blur $BLUR $PICTURE
betterlockscreen -u $PICTURE --blur 2 -l
rm $PICTURE
