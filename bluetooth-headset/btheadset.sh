#!/usr/bin/env bash
# Copyright (C) 2015 Valentin Rusu <vrusu@fsfe.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# you could specify here your headset's ID so you could invoke this script
# withouf the last parameter
HEADSET_ID=""

# you may adjust the desired PulseAudio profile here but this defaults means
# High Fidelity Playback, so you may want to keep it this way
HEADSET_PROFILE="a2dp_sink"

# SCRIPT BEGINS HERE, modify on your own risk ;-)
STATUS_CONNECTED="connected"
STATUS_DISCONNECTED="disconnected"

if [ "x$1" == "x" ]; then
  echo "Usage:"
  echo "  btheadset on|off|status [DEVICE_ID]"
  echo ""
  exit 1
fi

if [ ! "x$2" == "x" ]; then
  HEADSET_ID=$2
fi

if [ "x$HEADSET_ID" == "x" ]; then
  echo "DEVICE_ID was not set, so quitting now."
  exit 1
fi

function set_profile()
{
IDXS=($(pacmd list-cards | grep 'index' | cut -d ':' -f 2))
DEVS=($(pacmd list-cards | grep 'device.string' | cut -d '=' -f 2))
for i in "${!DEVS[@]}"
do
  # NOTE the device string returned by pacmd has double-quotes around it
  if [ "${DEVS[i]}" == "\"$HEADSET_ID\"" ]; then
    pacmd set-card-profile ${IDXS[i]} "$HEADSET_PROFILE"
    [ ! $? -eq 0 ] && echo "Cannot set pulseaudio profile" && exit 1
    echo "profile successfully changed"
  fi
done
}

function show_status()
{
INFO_STRING=$( sudo bluetoothctl <<EOF
info $HEADSET_ID
EOF
)
STATUS=$(echo "$INFO_STRING" | grep "Connected" | cut -d ":" -f 2 | tr -d '[[:space:]]')
[ "$STATUS" == "yes" ] && echo $STATUS_CONNECTED && exit 0
[ "$STATUS" == "no" ] && echo $STATUS_DISCONNECTED && exit 0
echo "Unknown status $STATUS" && exit 1
}

function wait_status()
{
STATUS=$(show_status)
count=0
while [ ! "$STATUS" == "$1" ]; do
  sleep 1
  STATUS=$(show_status)
  ((count++))
  [ $count -gt 20 ] && echo "Timeout waiting for $1 event" && exit 1
done
}

function connect()
{
INFO_STRING=$( sudo bluetoothctl <<EOF
connect $HEADSET_ID
EOF
)
[ ! $? -eq 0 ] && exit $?
wait_status $STATUS_CONNECTED
set_profile
show_status
}

function disconnect()
{
INFO_STRING=$( sudo bluetoothctl <<EOF
disconnect $HEADSET_ID
EOF
)
[ ! $? -eq 0 ] && exit $?
wait_status $STATUS_DISCONNECTED
show_status
}

case "$1" in
  on)
    connect
    ;;
  off)
    disconnect
    ;;
  status)
    show_status
    ;;
  *)
    echo "Unkown command $1"
    exit 1
esac
