#! /bin/sh

width=200
height=200
datefmt="+%a %d.%m.%Y %H:%M:%S"

OPTIND=1
while getopts ":f:W:H:" opt; do
    case $opt in
        f) datefmt="$OPTARG" ;;
        W) width="$OPTARG" ;;
        H) height="$OPTARG" ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
    esac
done

case "$BLOCK_BUTTON" in
  1|2|3) 

	# the position of the upper left corner of the popup
	posX=$(($BLOCK_X - $width / 2))
	posY=$(($BLOCK_Y - $height))

	i3-msg -q "exec yad --calendar \
        --width=$width --height=$height \
	    --undecorated --fixed \
	    --close-on-unfocus --no-buttons \
	    --posx=$posX --posy=$posY \
	    > /dev/null"
esac
date "$datefmt"
