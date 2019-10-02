# xkb_layout

Keyboard layout indicator.

Monitors for layout change and refreshes on its own without need for signals from i3blocks. Does not handle clicks or switch layouts.

![block preview](xkb_layout.png)

# Requires:

 - [xkb-switch](https://github.com/ierton/xkb-switch) utility, should be in your distro's package repository under the same name.

 - A standard X11 way of switching layouts you would use anyways:

```
exec --no-startup-id "setxkbmap -layout us,ru -option 'grp:alt_shift_toggle'"
```

The above line needs to be executed after X session startup, add it to `~/.config/i3/config` or `~/.xsession` or any other place you manage startup apps and scripts in.

# i3blocks config example:

```ini
[xkb_layout]
command=$SCRIPT_DIR/xkb_layout
font=monospace
font_weight=bold
interval=persist
markup=pango
```

`font` must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant font name. If not set, 'monospace' is used as default.

`font_weight` must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant font weight. If not set, 'bold' is used as default.
