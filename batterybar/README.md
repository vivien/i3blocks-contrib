# i3blocks battery bar
	
What does it do ?
-----------------

It displays the battery level in a set of five unicode squares (U+25A0).

It also changes color for more accuracy and to distinguish between charging, 
discharging, charged and AC statuses.

You can also specify your own set of colors.
	
Left-clicking briefly shows the battery level in percent.

Installation
------------

* Copy the batterybar script into your directory of choice, e.g. ~/.i3blocks/
* Give it execution permission (`chmod +x batterybar`)
* Add the following blocket to your i3blocks.conf:

```ini
[batterybar]
command=$SCRIPT_DIR/batterybar #run batterybar -h for options
label=bat:
interval=5
markup=pango
min_width=bat: ■■■■■
```
	
Dependencies
------------

* acpi
