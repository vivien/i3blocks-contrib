#!/usr/bin/env bash

################################
# Shows info about screen brightness.
# Allows simple brightness controls.
#
# By Thomas MEREL <thomas.merel.44@gmail.com>
# Base on @EliteTK sound manager for i3blocks
#
# Dependencies:
# - xbacklight
# - ttf-font-icons
#
# @return {Number}: Current screen luminosity
################################

dir=$(dirname $0)
source $dir/util.sh

full=""
short=""
status=0

step=${BLOCK_INSTANCE:-5}

getBrightness() {
	xbacklight
}


case $BLOCK_BUTTON in
	# scroll up
	# raise bright
	4) xbacklight -inc $step >/dev/null ;;

	# scroll down
	# lower bright
	5) xbacklight -dec $step >/dev/null ;;
esac

light=$(getBrightness)

# level-based icon
if (( $light == 0 )); then
#	no bright
	icon=""
elif (( $light < 50 )); then
#	low bright
	icon=""
elif (( $light < 100)); then
#	high bright
	icon=""
else
#	full bright
	icon=""

fi

full="$icon ${light%.*}%"
short=$light

echo $full
echo $short
exit $status
