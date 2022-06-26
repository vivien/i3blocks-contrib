#!/usr/bin/env bash
###### Default environment variables ######
IDLE_TEXT=${IDLE_TEXT:-CPICK}
IDLE_TEXT_COLOR=${IDLE_TEXT_COLOR:-#FFFFFF}

###### Verify dependencies ######
if ! command -v xdotool &> /dev/null || ! command -v grabc &> /dev/null; then
  error 'xdotool and/or grabc is not available'
  exit 1
fi

###### Functions ######
error() {
  echo Error: "$@" 1>&2
}

play_pause() {
  $running && pause || play
}

play() {
  running=true
  pickcolor
}

pause() {
  running=false
  fgcolor="$IDLE_TEXT_COLOR"
}

hash2hex() {
  echo "${1/\#/0x}"
}

subtract_colors() {
  col1=$(hash2hex "$1")
  col2=$(hash2hex "$2")
  b1=$(( col1 % 0x000100 ))
  g1=$(( (col1 % 0x010000 - b1) / 0x100 ))
  r1=$(( (col1 % 0x1000000 - 0x100*g1 - b1) / 0x10000 ))
  b2=$(( col2 % 0x000100 ))
  g2=$(( (col2 % 0x010000 - b2) / 0x100 ))
  r2=$(( (col2 % 0x1000000 - 0x100*g2 - b2) / 0x10000 ))
  dr=$(( r2 - r1 ))
  dg=$(( g2 - g1 ))
  db=$(( b2 - b1 ))
  echo $(( ${dr#-} + ${dg#-} + ${db#-} ))
}

rgbcmybw=(
  [0]='#ff0000'
  [1]='#00ff00'
  [2]='#0000ff'
  [3]='#ffff00'
  [4]='#ff00ff'
  [5]='#00ffff'
  [6]='#000000'
  [7]='#ffffff')

pickcolor() {
  > /dev/null 2>&1 xdotool sleep 0.01 click 1 &
  bgcolor=$(grabc 2> /dev/null)
  col_diff_max=0
  col_diff=0
  for col in "${rgbcmybw[@]}"; do
    col_diff=$(subtract_colors "$col" "$bgcolor")
    if (( ${col_diff#-} > "$col_diff_max" )); then
      fgcolor=$col
      col_diff_max=${col_diff#-}
    fi
  done
}

###### Initialize ######
[[ ! -v running ]] && pause

###### Click processing ######
case $BLOCK_BUTTON in
  1 )
    play_pause
    ;;
esac

###### Update color ######
if $running; then
  pickcolor
  bgcolorstring='"background":"'"$bgcolor"'"'
else
  bgcolor="$IDLE_TEXT"
  bgcolorstring=
fi

###### Output ######
cat << EOF
{"full_text":"$bgcolor",\
"running":"$running",\
"bgcolor":"$bgcolor",\
"fgcolor":"$fgcolor",\
"color":"$fgcolor",\
$bgcolorstring\
}
EOF
