#!/usr/bin/env bash
#
# Copyright (C) 2016 James Murphy
# Licensed under the terms of the GNU GPL v2 only.
#
# i3blocks blocklet script to monitor disk io

label="${LABEL:-""}"
dt="${DT:-5}"
MB_only="${MB_ONLY:-0}"
kB_only="${KB_ONLY:-0}"
width="${WIDTH:-4}"
MB_precision="${MB_PRECISION:-1}"
kB_precision="${KB_PRECISION:-0}"
regex="${REGEX:-$BLOCK_INSTANCE}"
regex="${regex:-/^(s|h)d[a-zA-Z]+/}"
threshold="${THRESHOLD:-0}"
warn_color="${WARN_COLOR:-#FF0000}"
sep="${SEPARATOR:-/}"
unit_suffix="${SUFFIX:-B/s}"
align="${ALIGN--}"

function list_devices {
    echo "Devices iostat reports that match our regex:"
    iostat | awk '$1~/^(s|h)d[a-zA-Z]+/{print $1}'
}

while getopts L:t:w:p:P:R:s:ST:C:lLMmKkh opt; do
    case "$opt" in
        L) label="$OPTARG" ;;
        t) dt="$OPTARG" ;;
        w) width="$OPTARG" ;;
        p) kB_precision="$OPTARG" ;;
        P) MB_precision="$OPTARG" ;;
        R) regex="$OPTARG" ;;
        s) sep="$OPTARG" ;;
        S) unit_suffix="" ;;
        T) threshold="$OPTARG" ;;
        C) warn_color="$OPTARG" ;;
        l) list_devices; exit 0 ;;
        M|m) MB_only=1 ;;
        K|k) kB_only=1 ;;
        h) printf \
"Usage: disk-io [-t time] [-w width] [-p kB_precision] [-P MB_precision] [-R regex] [-s separator] [-S] [-T threshold [-C warn_color]] [-k|-M] [-l] [-h]
Options:
-L\tLabel to put in front of the text. Default: $label
-t\tTime interval in seconds between measurements. Default: $dt
-w\tThe width of printed floats. Default: $width 
-p\tThe precision of kB/s floats. Default: $kB_precision 
-P\tThe precision of MB/s floats. Default: $MB_precision
-R\tRegex that devices must match. Default: $regex
-s\tSeparator to put between rates. Default: $sep
-S\tShort units, omit B/s in kB/s and MB/s.
-T\tRate in kB/s to exceed to trigger a warning. Default: not enabled
-C\tColor to change the blocklet to warn the user. Default: $warn_color
-l\tList devices that iostat reports
-M\tDo not switch between MB/s and kB/s, use only MB/s
-k\tDo not switch between MB/s and kB/s, use only kB/s
-h\tShow this help text
" && exit 0;;
    esac
done

iostat -dyz "$dt" | awk -v sep="$sep" "
    BEGIN {
        rx = wx = 0;
    }
    {
        if(\$0 == \"\") {
            if ($threshold > 0 && (rx >= $threshold || wx >= $threshold)) {
                printf \"<span color='$warn_color'>\";
            }
            printf \"$label\";
            if(!$kB_only && ($MB_only || rx >= 1024 || wx >= 1024)) {
                printf \"%$align$width.${MB_precision}f%s%$width.${MB_precision}f M$unit_suffix\", rx/1024, sep, wx/1024;
            }
            else {
                printf \"%$align$width.${kB_precision}f%s%$width.${kB_precision}f k$unit_suffix\", rx, sep, wx;
            }
            if ($threshold > 0 && (rx >= $threshold || wx >= $threshold)) {
                printf \"</span>\";
            }
            printf \"\n\";
            fflush(stdout);
        }
        else if(\$1~/^Device:?/) {
            rx = wx = 0;
        }
        else if(\$1~$regex) {
            rx += \$3;
            wx += \$4;
        }
    }"
