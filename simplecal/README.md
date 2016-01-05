# simplacal

Simplecal is extremely easy way how to show the calendar applet after clicking on time blocklet

![](screen.jpg?raw=true)


# Requirements

Dependencies:  bash, calendar applet

Suggested: fonts-font-awesome
 
# i3blocks sutup

```
[time]
#label=
label=time:
command=$SCRIPT_DIR/simplecal
interval=5

```

# Calendar setup

I chose [Gsimplecal](https://github.com/dmedvinsky/gsimplecal)

## Instalation

Debian/Ubuntu - apt-get install gsimplecal

## Setup

Create "config" file in "~/.config/gsimplecal" with content:

```
mark_today = 1
close_on_unfocus = 1

```

Calendar applet is shown after clicking on the time blocklet and hides itself after unfocus. The default calendar position is the position of the cursor.


