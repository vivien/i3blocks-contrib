

# system-button

Creates a button for powering down, rebooting, suspending or hibernating the
system.

![](poweroff.png) ![](reboot.png) ![](suspend.png) ![](hibernate.png)
![](error.png)


# Dependencies

- The [bash](https://www.gnu.org/software/bash/bash.html) shell or a
compatible one.

- A mouse with at least three buttons. A scroll wheel counts as two buttons,
as three or four if clickable.


# Optional

- [systemd](https://freedesktop.org/wiki/Software/systemd/) or
[elogind](https://github.com/elogind/elogind) for the ``systemctl`` and/or
``loginctl`` commands.

- [Font Awesome](https://fontawesome.com) for the default
label icons.

- [libnotify](https://developer.gnome.org/notification-spec/) for
error notifications via ``notify-send``.


# Usage

Scrolling the mouse wheel selects the action to take, left-clicking
tries to perform it.  In case of inhibiting factors like other
user sessions, the action is not performed and the blocklet displays an
error label ( ![](error.png) ). Right-clicking forces the action to be
performed anyway. For non-standard mouse button layouts, button numbers are
configurable. If the selected action fails, an error label
is displayed and if available, ``notify-send`` is used
to send a notification.

The default commands for actions are the standard ``systemctl`` resp.
``loginctl`` subcommands. They can be overridden by configuration variables
named *ACTION*_``CMD``, which is mandatory if neither ``systemctl`` nor
``loginctl`` are available.

A pango font fallback must be set in the window manager's bar
configuration ([see the i3blocks FAQ](https://github.com/vivien/i3blocks#faq)).
It should include FontAwesome for the default labels to be displayed correctly.

The "force action" and "scroll back" mouse buttons are configurable. If they
are set, they must both not be 1 and obviously different from each other.


# Config

```INI
[system-button]
## For a standard installation of i3blocks-contrib, i.e.
##
## make install
## status_command SCRIPT_DIR=<installation directory> i3blocks  # in the window manager's bar config
## command=$SCRIPT_DIR/$BLOCK_NAME  # as a global i3blocks config property
##
## no command property is needed here. 
#command=$SCRIPT_DIR/system-button
color=#c80000
background=#000000
align=center
min_width=XX
interval=persist
markup=pango
## These commands must be defined if neither systemd nor elogind are running.
## The user id of the i3blocks process must have permission to execute them:
#POWEROFF_CMD=
#REBOOT_CMD=
#SUSPEND_CMD=
#HIBERNATE_CMD=
## The mouse button defaults are set for models with two buttons and a clickable
## wheel. Button 1 is always the regular action trigger, two are configurable
## here and all others scroll forward through the actions.
#FORCE_ACTION_BUTTON=3
#SCROLL_BACK_BUTTON=4
## The default labels need font-awesome. Spaces are ok,
## ',' ':' '\' '$' '`' are not allowed.
#POWEROFF_LABEL=
#REBOOT_LABEL=
#SUSPEND_LABEL=
#HIBERNATE_LABEL=
#ERROR_LABEL=
```
