#! /bin/sh

DATEFTM="${DATEFTM:-+%a. %d. %b. %Y}"
SHORTFMT="${SHORTFMT:-+%d.%m.%Y}"
LABEL="${LABEL:-}"
blockdate=$(date "$DATEFTM")
shortblockdate=$(date "$SHORTFMT")

year=$(date '+%Y')
month=$(date '+%m')
case "$BLOCK_BUTTON" in
    1|2)
        date=$(date '+%A, %d. %B');;
    3)
        (( month == 12 )) && month=1 && year=$((year + 1)) || month=$((month + 1))
        date=$(cal $month $year | sed -n '1s/^  *//;1s/  *$//p')
esac
case "$BLOCK_BUTTON" in
    1|2|3)
export TERM=xterm
cal --color=always $month $year \
    | sed 's/\x1b\[[7;]*m/\<b\>\<u\>/g' \
    | sed 's/\x1b\[[27;]*m/\<\/u\>\<\/b\>/g' \
    | tail -n +2 \
    | rofi \
        -dmenu \
        -markup-rows \
        -no-fullscreen \
        -font "Monospace 6" \
        -hide-scrollbar \
        -bw 2 \
        -m -3 \
        -theme-str '#window {anchor:southeast; location: northwest;}' \
        -eh 1 \
        -width -22 \
        -no-custom \
        -p "$date" > /dev/null 
    esac
echo "$LABEL$blockdate"
echo "$LABEL$shortblockdate"
