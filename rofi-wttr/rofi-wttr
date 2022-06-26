#! /usr/bin/env bash

###### Variables ######
LABEL="${LABEL:- }"
LOCATION="${LOCATION:- }"
FONT="${FONT:-Monospace 10}"
ROFI_CONFIG_FILE="${ROFI_CONFIG_FILE:-/dev/null}"
BAR_POSITION="${BAR_POSITION:-bottom}"

###### Variables ######


###### Functions ######
# print the full weather
# see https://github.com/chubin/wttr.in#usage for full configuration options
print_weather_report() {
  if [[ $LOCATION != " " ]]; then
    curl https://wttr.in/$LOCATION?T
  else
    curl https://wttr.in/?T
  fi
}

# print the one line weather
# see https://github.com/chubin/wttr.in#one-line-output for formatting options
print_weather_line() {
  if [[ $LOCATION != " " ]]; then
    curl -s https://wttr.in/${LOCATION}?u\&format="%C+%c+%t+(%f)+%w" | tr -d \"
  else
    curl -s 'https://wttr.in/?u\&format="%C+%c+%t+(%f)+%w"' | tr -d \"
  fi
}

###### Functions ######


###### Main body ######

# handle any click
# rofi pop up
case "$BLOCK_BUTTON" in
  1|2|3)
      IFS=
      weather_report=$(print_weather_report)

      # check bar position and adjust anchor accordingly
      if [[ $BAR_POSITION = "top" ]]; then
        anchor="northwest"
      else
        anchor="southwest"
      fi

      # open rofi
      # (add the following option to rofi command with proper config file, if needed)
      echo $weather_report \
        | rofi \
            -dmenu \
            -markup-rows \
            -font $FONT \
            -m -3 \
            -theme-str 'window {width: 53%; anchor: '"$anchor"'; location: northwest;}' \
            -theme-str 'listview {lines: '"$(echo $weather_report | wc -l)"' ;scrollbar: false;}' \
            -theme $ROFI_CONFIG_FILE \
            -p "Detailed weather report"
esac

# print blocklet text

if [[ $LABEL != " " ]]; then
  echo $LABEL$(print_weather_line)
else
  echo $(print_weather_line)
fi

###### Main body ######
