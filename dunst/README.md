# dunst

Creates a do-not-disturb button for muting [dunst](https://dunst-project.org/) notifications.

![](dunst.gif)


# Dependencies

- [dunst](https://dunst-project.org/)
- [Font Awesome](https://fontawesome.com) for the [bell](https://fontawesome.com/icons/bell?style=solid) and [bell-slash](https://fontawesome.com/icons/bell-slash?style=solid) icons


# Usage

Clicking the bell icon will toggle dunst notifications from being displayed.

This is accomplished by sending ```notify-send``` the special ```DUNST_COMMAND_PAUSE``` or ```DUNST_COMMAND_RESUME``` message.


# Config

```INI
[dunst]
command=$SCRIPT_DIR/dunst
interval=once
format=json
markup=pango
#min_width=50
#align=center
#DUNST_MUTE=off
```

