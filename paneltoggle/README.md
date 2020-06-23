# Description

Currently works for Asus Xonar DGX.
Toggles between the front and the back panel on click.
Displays a speaker or headphone depending on which panel is used.

# i3blocks.conf

```
[paneltoggle]
command=$SCRIPT_DIR/paneltoggle
interval=once
signal=5
```
signal can be whatever

## using a keyboard shortcut with a signal

put the togglepanel script in folder within your PATH variable, for example /bin/.
the togglepanel script can be used without i3blocks too.

```
bindsym XF86Tools exec --no-startup-id togglepanel && pkill -RTMIN+5 i3blocks
```

# TODO

- more refactoring
