#!/usr/bin/env bash
#
# i3blocks blocklet script to display wifi signal in dBm

if [[ -z "$IFACE" ]] ; then
    IFACE="${BLOCK_INSTANCE:-wlan0}"
fi

USE_PERCENT=${USE_PERCENT:-0}

IW=$(which iw || echo "/sbin/iw")

if [[ ! -x $IW ]]; then
	echo "No iw binary was found on the system." 1>2
	exit 1
fi

while getopts p opt; do
    case "$opt" in
        p) USE_PERCENT=1 ;;
    esac
done

dbm=$($IW dev "$IFACE" link | grep 'dBm$' | grep -Eoe '-[0-9]{2}')

[[ -n "$dbm" ]] || exit 1

if [[ $USE_PERCENT -eq 0 ]]; then
    echo "$dbm" dBm
    echo "$dbm"
else
    if [[ "$dbm" -le -100 ]]; then
        quality=0
    elif [[ $dbm -ge -50 ]]; then
        quality=100
    else
        quality=$((2 * (dbm + 100)))
    fi
    echo "$quality%"
    echo "$quality%"
fi

if [[ $dbm -ge -55 ]]; then
	echo "#00FF00"
elif [[ $dbm -ge -60 ]]; then
	echo "#CCFF00"
elif [[ $dbm -ge -70 ]]; then
	echo "#FFFF00"
elif [[ $dbm -ge -80 ]]; then
	echo "#FFAA00"
else
	echo "#FF0000"
fi
