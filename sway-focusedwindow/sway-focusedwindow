#!/usr/bin/env bash

maxlen=0
if [[ $1 ]]; then
  maxlen=$1
fi

align="center"
if [[ $2 ]]; then
  align=$2
fi

format() {
  if [[ $maxlen == 0 ]]; then
    echo "$1"
    return 0
  fi
  len=${#1}
  if [[ $len -ge $maxlen ]]; then
    echo "${1:0:${maxlen}}"
  else
    pad=$(( maxlen - len ))
    case "$align" in
      "center" )
        pad=$(( pad / 2 ))
        printf "%*s%s%*s\n" $pad "" "$1" $pad ""
        ;;
      "left" )
        printf "%s%*s\n" "$1" $pad "" 
        ;;
      "right" )
        printf "%*s%s\n" $pad "" "$1"
        ;;
    esac
  fi
}

process() {
  while read -r LINE; do
    format "$LINE"
  done
}

swaymsg -t get_tree | jq --unbuffered -r '.. | select(.focused?) | .name' | process

subscribe_query='select(.container.focused and (.change == "focus" or .change == "title")) | .container.name'
swaymsg -m -t SUBSCRIBE "['window']" | jq --unbuffered -r "$subscribe_query" | process
