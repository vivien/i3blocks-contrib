# arch-update

Be always on top of your available updates with this blocklet. Optionally show AUR updates with the help of yaourt. Colorize the outputs for if your system is up to date or you got available updates.

![](screenshot.png)

![](screenshot2.png)
	
# Dependencies

* Arch Linux or another arch based distro
* python3

# Optional Dependencies

* yaourt for aur updates
* fontawesome for awesome labels

# Installation

* Copy the arch-update.py script into your directory of choice, e.g. ~/.i3blocks/
* Give it execution permission (`chmod +x arch-update.py`)
* Add the following blocket to your i3blocks.conf:

```ini
[arch-update]
command=$SCRIPT_DIR/arch-update.py #run arch-update.py -h for options
label=Updates:
interval=3600
markup=pango
```
Another advanced example with fontawesome label, AUR updates included and custom colors for both messages:
```ini
[pacman-updates]
label=
command=~/.config/i3blocks/scripts/arch-update.py -a -b "#5fff5f" -u "#FFFF85"
markup=pango
interval= 3600
```
# Configuration
- `-b`/`--base_color`: set the base color of the output (when your system is up to date)
- `-u`/`--updates_available_color`: set the color of the output when updates are available
- `-a`/`--aur`: activate AUR update support  
For the latest options call `$SCRIPT_DIR/arch-update.py -h`.
