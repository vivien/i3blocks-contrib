#! /bin/sh

case "$BLOCK_BUTTON" in
  1|2|3) 
	# get the current mouse position
	mouseX=$(xdotool getmouselocation | cut -d' ' -f1 | cut -c3-)
	mouseY=$(xdotool getmouselocation | cut -d' ' -f2 | cut -c3-)

	# these are the dimensions of the popup window (at least on my machine)
	# you can check them with xwininfo
	windowWidthX=$((172))
	windowWidthY=$((184))

	# the position where I want upper left corner of the popup
	posX=$(($mouseX - $windowWidthX / 2))
	posY=$(($mouseY - $windowWidthY))

	yad --calendar \
	    --undecorated --fixed \
	    --close-on-unfocus --no-buttons \
	    --posx=$posX --posy=$posY \
	    > /dev/null # don't show the output in the status bar
esac
date '+%a %d.%m.%Y %H:%M:%S'
