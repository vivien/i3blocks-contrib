<center>i3blocks battery bar</center>
						
	
What does it do ?
-----------------
It displays the battery level in a set of five unicode squares (U+25A0).<br>
It also changes color for more accuracy and to distinguish between<br>
charging, discharging, charged and AC statuses.<br>
	
Left-clicking briefly shows the battery level in percent.<br>

Installation
------------
<ol>

<li> Copy the battery_bar script into /usr/share/i3blocks/.<br>
<li> Give it execution permission. (`#chmod +x battery_bar`).<br>
<li> Add the following blocket to your i3blocks.conf:<br>

```
[batterybar]
label=bat:
interval=5
markup=pango
min_width=bat: ■■■■■
```
	
Dependencies
-------------
perl, acpi
	

	
	
