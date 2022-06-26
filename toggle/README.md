# toggle

Toggle button. Supports arbitrary commands to toggle on, off, and get current
toggle status.

On: ![](toggle_on.png)

Off: ![](toggle_off.png)

# Requirements

None

# Configuration

A toggle config block includes a label and commands for each of:

*   Turning the toggle on
*   Turning the toggle off
*   Checking the current toggle status (exit code 0 indicates 'on')

For example, a configuration to toggle the
[wayvnc VNC server](https://github.com/any1/wayvnc) might look like this:

```INI
[toggle]
label=
command=$SCRIPT_DIR/toggle
interval=once
COMMAND_ON=swaymsg -q exec wayvnc localhost
COMMAND_OFF=kill $(ps -e -o pid -o exe | grep $(which wayvnc) | awk '{print $1}')
COMMAND_STATUS=ps -eo exe | grep $(which wayvnc)
#COLOR_ON=#ffffff
#COLOR_OFF=#5f6368
```

## Configuration Parameters

Parameter      | Description
-------------- | -----------
COMMAND_ON     | Required: The command to turn the toggle 'on'
COMMAND_OFF    | Required: The command to turn the toggle 'off'
COMMAND_STATUS | Required: The command to check the current toggle status (exit code 0 indicates currently on)
COLOR_ON       | Optional: The color to use when the toggle is 'on'. Uses the default color if unspecified
COLOR_OFF      | Optional: The color to use when the toggle is 'off'. Uses dark gray (#555555) if unspecified

The script takes care of suppressing output from each of the commands. If you
want to run a command that doesn't immediately exit, it will lock the script
unless you ask i3 (or Sway) to run it for you with i3-msg (or swaymsg).
