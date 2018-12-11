# rofi-arch-update

Have a list of available updates pop up in rofi when clicking the arch update blocklet

![](screenshot.png)
# Dependencies

* rofi
# Installation

* Copy the script into your directory of choice, e.g. ~/.i3blocks/blocklets
* Give it execution permission (`chmod +x rofi-arch-update`)
* Edit rofi launch options in the script to fit your needs
* Add the following blocklet to your i3blocks.conf:

```ini
[rofi-arch-update]
command=$SCRIPT_DIR/rofi-arch-update
interval=3600
markup=pango
LABEL= 
#ROFI_CONFIG=~/.config/rofi/blue.rasi
#ROFI_HEADER="update(s) available"
#UP_TO_DATE_COLOR=green
#UPDATES_AVAIL_COLOR=yellow
#UP_TO_DATE_TEXT=up to date
#ONE_UPDATE_TEXT=update
#MORE_UPDATES_TEXT=updates
#UP_TO_DATE_PRE_TEXT=system
#UPDATES_AVAIL_POST_TEXT=available
```
