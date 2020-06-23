# Description

Currently works for Asus Xonar DGX.
Toggles between the front and the back panel on click.
Displays a speaker or headphone depending on which panel is used.

# i3blocks.conf

```
[paneltoggle]
command=$SCRIPT_DIR/paneltoggle
interval=once
```

- set `interval` to a time in seconds if you use a keyboard shortcut

# TODO

- more refactoring
