# Customizable disk block for i3blocks

Script checks the disk usage of **$BLOCK_INSTANCE** using pythons **os.statvfs** module. If the instance isn't set the home-directory of the executing user will be set as default.

So a standard configuration minding a specific partition would look as follows:

```
[disk_nas]
label=:
instance=/nas
interval=30
command=$SCRIPT_DIR/disk_usage/disk_usage
```

## Arguments

Additionally the script can take more arguments passed to it by command-line in a key=value fashion. The following is supported.

### Warning Threshold
The warning threshold in percent (used disk space).

Display warnig color when 70% of the available disk space is used:
``
warn_threshold=70
``

_Default:_ 80

### Critical Threshold
The critical threshold in percent (used disk space)

Display critical color when 80% of the available disk space is used:
``
crit_threshold=80
``

_Default:_ 90

### Warning Color
Hex-color code to use when **warn_threshold** is reached:
``
warn_color=#90ce00
``

_Default:_ #d6af4e

### Critical Color
Hex-color code to use when **crit_threshold** is reached:
``
crit_color=#ce2500
``

_Default:_ #d64e4e

### Output Format
Output format used by pythons string formatting for displayment.

To get:
```
: 119.3G used of 518.5 total beeing 23.0%
```

the following *format*-argument must be passed to the script:

```
format="{used:.1f}G used of {total:.1f} total beeing {perc_used}%"
```
Quotes are required for format.

#### Fields

* **avail:** available disk space in gigabytes
* **used:** used disk space in gigabytes
* **total:** total diskspace in gigabytes
* **perc_used:** disk usage in percent

## Example

```
[disk_root]
label=:
instance=/
interval=30
command=$SCRIPT_DIR/disk_usage/disk_usage format="{used:.1f}G used of {total:.1f} Total beeing {perc_used}%" warn_color=#90ce00
```

## Click events

Upon a click event a terminal is opened with ncdu running for the configured partition. To adapt this to your personal setup, you'll need to change the function **launch_ncdu()**:

```python
def launch_ncdu(mp):
	cmd = [
		'/usr/bin/sakura',
		'-t',
		'pop-up',
		'-e',
		'/usr/bin/ncdu %s' % mp,
		'-x',
	]

	subprocess.Popen(
		cmd,
		stdout=open(os.devnull, 'w'),
		stderr=subprocess.STDOUT
	)
```

Personally, I launch sakura with *pop-up* as title, which i can then use to configure i3 to set the window into floating mode:

```
for_window [title="pop-up"] floating enable border none sticky
```

Output of the launch-command will be redirected to /dev/null

## Dependancies

The script uses only standard python modules and should therefore run on any python environment or should easily be made to run.

## Help

* Advanced String Formatting: https://www.python.org/dev/peps/pep-3101/

## Screenshot

![screenshot][screenshot]

[screenshot]: https://raw.githubusercontent.com/nevious/i3blocks_blocklets/master/disk_usage/screenshot.png
