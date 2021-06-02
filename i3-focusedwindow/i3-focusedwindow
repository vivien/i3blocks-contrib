#!/usr/bin/env bash
# Author: Kn

while :
do
  ID=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
  if [[ $1 ]] 
  then
    TITLE=$(xprop -id $ID -len $1 | awk '/_NET_WM_NAME/{$1=$2="";print}' | cut -d'"' -f2)
    echo "$TITLE"
  else
    TITLE=$(xprop -id $ID | awk '/_NET_WM_NAME/{$1=$2="";print}' | cut -d'"' -f2)
    echo "$TITLE"
  fi
done
