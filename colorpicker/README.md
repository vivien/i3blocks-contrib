# colorpicker

Minimal colorpicker blocklet. Left click to start and to pause.

Requires [grabc](https://github.com/muquit/grabc) and [xdotool](https://archlinux.org/packages/community/x86_64/xdotool/).

![](colorpicker.png)

* Copy the script into your directory of choice, e.g. ~/.i3blocks/blocklets
* Give it execution permission (`chmod +x colorpicker`)
* Add the following blocklet to your i3blocks.conf:

```ini
[colorpicker]
format=json
interval=1
#IDLE_TEXT=CPICK
#IDLE_TEXT_COLOR=#FFFFFF
```
