# rofi-calendar

Have a minimal calendar pop up in rofi when clicking the date blocklet (right click to show next month)

![](screenshot.png)

![](screenshot2.png)
	
# Dependencies

* rofi 
* cal from util-linux package, supporting --color=always
# Installation

* Copy the script into your directory of choice, e.g. ~/.i3blocks/blocklets
* Give it execution permission (`chmod +x rofi-calendar`)
* Edit rofi launch options in the script to fit your needs
* Add the following blocklet to your i3blocks.conf:

```ini
[rofi-calendar]
command=$SCRIPT_DIR/rofi-calendar
interval=3600
LABEL= 
#DATEFTM=+%a. %d. %b. %Y
#SHORTFTM=+%d.%m.%Y
```

