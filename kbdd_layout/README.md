#kbdd_layout

![view of block](block.png)

This blocklet gets [kbdd](https://github.com/qnikst/kbdd) layout throught dbus service in real time mode.

kbdd is a useful daemon made for lightweight window managers. It works with xkb and remember layout for windows.

The blocklet needs running kbdd and it works properly even if setxkbmap does not show your current layout.

```ini
[kbdd_layout]
command=$SCRIPT_DIR/kbdd_layout
interval=-3
```

Keep in mind, that interval should be '-3' (that means persist), so the blocklet does not support short text and color strings.
