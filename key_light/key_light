#!/usr/bin/env bash

# Copyright 2019 Matej Čamaj <camaj at protonmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# See https://upower.freedesktop.org/docs/KbdBacklight.html
function get_brightness {
    dbus-send --system --type=method_call --print-reply\
        --dest="org.freedesktop.UPower" \
        "/org/freedesktop/UPower/KbdBacklight" \
        "org.freedesktop.UPower.KbdBacklight.$1" \
        |  awk 'FNR==2{print $2}'
}

brightness=$(get_brightness "GetBrightness")
max_brightness=$(get_brightness "GetMaxBrightness")

if [ "$brightness" -eq "$max_brightness" ]; then
   new_brightness=0
else
   new_brightness=$((brightness + 1))
fi

dbus-send --system --type=method_call \
    --dest="org.freedesktop.UPower" \
    "/org/freedesktop/UPower/KbdBacklight" \
    "org.freedesktop.UPower.KbdBacklight.SetBrightness" int32:$new_brightness
