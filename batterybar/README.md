<center>i3blocks battery bar</center>
						
	
What does it do ?
-----------------
It displays the battery level in a set of five unicode squares (U+25A0).<br>
It also changes color for more accuracy and to distinguish between<br>
charging, discharging, charged and AC statuses.<br>
	
Left-clicking briefly shows the battery level in percent.<br>

Installation
------------
1-Copy the battery_bar script into /usr/share/i3blocks/.<br>
2-Give it execution permission. (#chmod +x battery_bar).<br>
3-Add the following blocket to your i3blocks.conf:<br>

[battery_bar]<br>
label=bat:<br>
interval=5<br>
markup=pango<br>
min_width=bat: ■■■■■

	
Dependencies
-------------
perl, acpi
	
	
Bugs
----
Disappears on 80% only. 


	
	