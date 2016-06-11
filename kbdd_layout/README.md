# kbdd_layout

![view of block](block.png)

This blocklet gets [kbdd](https://github.com/qnikst/kbdd) layout through dbus service in real time mode.

kbdd is a useful daemon made for lightweight window managers. 
It works with xkb and remembers layouts for each window.

# Requirements

Dependencies: kbdd (typically in package of the same name).

You can set your keyboard configuration e.g. with

```
exec --no-startup-id "setxkbmap -layout us,ru -option 'grp:ctrl_alt_toggle'"
```

in your i3 config.
The blocklet must be restarted if you execute another setxkbmap command,
or it may give incorrect results.

# Config

```ini
[kbdd_layout]
command=$SCRIPT_DIR/kbdd_layout
interval=persist
```
