# kbdd_layout

Show keyboard layout using dbus and [kbdd](https://github.com/qnikst/kbdd).

![view of block](block.png)

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
