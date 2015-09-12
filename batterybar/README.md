<center>i3blocks battery bar</center>
						
	
What does it do ?
-----------------
It displays the battery level in a set of five unicode squares (U+25A0).<br>
It also changes color for more accuracy and to distinguish between<br>
charging, discharging, charged and AC statuses.<br>

You can also specify your own set of colors.<br>
	
Left-clicking briefly shows the battery level in percent.<br>

Installation
------------
<ol>

<li> Copy the batterybar script into your directory of choice, e.g. ~/.i3blocks/</li>
<li> Give it execution permission (`chmod +x batterybar`).</li>
<li> Add the following blocket to your i3blocks.conf:</li>

</ol>

```
[batterybar]
command=$SCRIPT_DIR/batterybar #run batterybar -h for options
label=bat:
interval=5
markup=pango
min_width=bat: ■■■■■
```
	
Dependencies
-------------
acpi
	

	
	
