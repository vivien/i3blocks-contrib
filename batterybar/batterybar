#!/usr/bin/env bash
#  batterybar; displays battery percentage as a bar on i3blocks
#  
#  Copyright 2015 Keftaa <adnan.37h@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



output=$(acpi battery)
percentage=$(echo "$output" | grep -o -m1 '[0-9]\{1,3\}%' | tr -d '%')
status=$(echo "$output" | egrep -o -m1 'Discharging|Charging|AC|Full|Unknown')
remaining=$( echo "$output" | egrep -o -m1 '[0-9][0-9]:[0-9][0-9]')
[[ -n $remaining ]] && remaining_formatted=" ($remaining)"
squares="■"


#There are 8 colors that reflect the current battery percentage when 
#discharging
dis_colors=("#FF0027" "#FF3B05" "#FFB923" "#FFD000" "#E4FF00" "#ADFF00"
			"#6DFF00" "#10BA00") 
charging_color="#00AFE3"
full_color="#FFFFFF"
ac_color="#535353"


while getopts 1:2:3:4:5:6:7:8:c:f:a:h opt; do
    case "$opt" in
        1) dis_colors[0]="$OPTARG";;
        2) dis_colors[1]="$OPTARG";;
        3) dis_colors[2]="$OPTARG";;
        4) dis_colors[3]="$OPTARG";;
        5) dis_colors[4]="$OPTARG";;
        6) dis_colors[5]="$OPTARG";;
        7) dis_colors[6]="$OPTARG";;
        8) dis_colors[7]="$OPTARG";;
        c) charging_color="$OPTARG";;
        f) full_color="$OPTARG";;
        a) ac_color="$OPTARG";;
        h) printf "Usage: batterybar [OPTION] color
        When discharging, there are 8 [1-8] levels colors.
        You can specify custom colors, for example:
        
        batterybar -1 red -2 \"#F6F6F6\" -8 green
        
        You can also specify the colors for the charging, AC and
        charged states:
        
        batterybar -c green -f white -a \"#EEEEEE\"\n";
        exit 0;
    esac
done



if (( percentage > 0 && percentage < 20  )); then
    squares="■"
elif (( percentage >= 20 && percentage < 40 )); then
    squares="■■"
elif (( percentage >= 40 && percentage < 60 )); then
    squares="■■■"
elif (( percentage >= 60 && percentage < 80 )); then
    squares="■■■■"
elif (( percentage >=80 )); then
    squares="■■■■■"
fi

if [[ "$status" = "Unknown" ]]; then
    squares="<sup>?</sup>$squares"
fi

case "$status" in
"Charging")
    color="$charging_color"
;;
"Full")
    color="$full_color"
;;
"AC")
    color="$ac_color"
;;
"Discharging"|"Unknown")
    if (( percentage >= 0 && percentage < 10 )); then
        color="${dis_colors[0]}"
    elif (( percentage >= 10 && percentage < 20 )); then
        color="${dis_colors[1]}"
    elif (( percentage >= 20 && percentage < 30 )); then
        color="${dis_colors[2]}"
    elif (( percentage >= 30 && percentage < 40 )); then
        color="${dis_colors[3]}"
    elif (( percentage >= 40 && percentage < 60 )); then
        color="${dis_colors[4]}"
    elif (( percentage >= 60 && percentage < 70 )); then
        color="${dis_colors[5]}"
    elif (( percentage >= 70 && percentage < 80 )); then
        color="${dis_colors[6]}"
    elif (( percentage >= 80 )); then
        color="${dis_colors[7]}"
    fi
;;
esac

if [[ "$BLOCK_BUTTON" -eq 1 ]]; then 
    echo "$status <span foreground=\"$color\">$percentage%$remaining_formatted</span>"
fi
    echo "<span foreground=\"$color\">$squares</span>" 
