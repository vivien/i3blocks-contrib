# rofi-xrandr

arandr style settings for multiple displays

![](screenshot.png)

![](screenshot2.png)
	
# Dependencies

* rofi 
* xrandr

# Installation

* Copy the script into your directory of choice, e.g. ~/.i3blocks/blocklets
* Give it execution permission (`chmod +x rofi-xrandr`)
* Edit rofi launch options in the script to fit your needs
* Add the following blocklet to your i3blocks.conf:

```ini
[rofi-xrandr]
command=$SCRIPT_DIR/rofi-xrandr
interval=once
```

