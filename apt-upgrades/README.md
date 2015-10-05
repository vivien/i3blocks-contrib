# i3blocks-apt-upgrades

i3blocks-apt-upgrades is an i3blocks blocklet script to show the number of pending system upgrades.

![](https://raw.githubusercontent.com/kb100/i3blocks-apt-upgrades/master/apt-upgrades.png)

# Requirements

Dependencies: aptitude, bash

Suggested: fonts-font-awesome

# Options

```
Usage: apt-upgrades [-s refresh_symbol] [-o] [-c refresh_color] [-N|-n nonrefresh_color] [-h]
Options:
-s  Specify a refresh symbol
-o  Show refresh symbol only, but no numbers
-c  Color when upgrade is pending
-n  Color when no upgrade is pending
-N  Only display text if upgrade is pending (supercedes -n)
-h  Show this help text
```
