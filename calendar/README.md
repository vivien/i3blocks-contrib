# calendar

Shows the current date and time. When clicked, a calendar popup is created.

This is similar to the rofi-calendar blocklet, but without the rofi dependency and with a slightly more advanced popup (at least in my opinion).

![](screenshot1.png)

![](screenshot2.png)

# Dependencies

* yad
* xdotool (for positioning of the popup)

# Installation

* Copy the script into your directory of choice, e.g. ~/.i3blocks/blocklets
* Give it execution permission (`chmod +x calendar.sh`)
* Add the script to your i3blocks.conf, for example like this:

```ini
[calendar]
command=$SCRIPT_DIR/calendar.sh
label=
interval=1
```

# Configuration

You may want to

* edit the date/time format
* change the placement of the popup
* change the parameters for `yad` to change the appearance of the popup
