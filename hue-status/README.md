# i3blocks-hue-status
i3blocks blocklet that shows status of a hue light, and has basic controls

I have just got this working as a proof of concept, and has a very limited feature set.

<p align="center">
  <img src="https://user-images.githubusercontent.com/9976046/37248460-bcbc0472-24ca-11e8-9885-183edd1a986a.png" alt="Pic of Color Picker"/>
</p>

### Latest Release
[Download from here](https://github.com/Rauwomos/i3blocks-hue-status/releases/latest)
This contains packaged apps thats saves you from downloading and installing dependencies. The source code is still here unless you want personalise it in any way

### Requirements
* font-awesome

### Sample i3blocks.conf
```
[light]
command=$SCRIPT_DIR/hue-status $SCRIPT_DIR/electron-hue-color-picker-linux-x64/electron-hue-color-picker
interval=1
markup=pango
```

### Add to i3 config
```
for_window [class="electron-hue-color-picker"] floating enable
```

### Controls
```
Left Click - On
Right Click - Off
Scroll Up - Increase brightness
Scroll Down - Decrease brightness
Middle Click - Select Colour
```

### Setup Instructions
1. Unzip the release to $SCRIPT_DIR
	* You should then have the following
		* $SCRIPT_DIR/hue-status
		* $SCRIPT_DIR/electron-hue-color-picker-linux-x64
	* You can put the hue-status executable wherever you want, just update your i3blocks config
	* If you change the location of the electron-hue-color-picker, add the new location as an argument in your i3blocks config
		* `command=/home/rowan/.config/i3/Light-Control/hue-status ~/.config/i3/electron-hue-color-picker-linux-x64/electron-hue-color-picker`
2. Add the require lines to i3blocks.conf and your i3 config

### Thinks to note with this version
1. I'm unsure how this will work with multi-monitor setups and am unable to test it
2. The first time you middle click it after boot, it will take longer to open up the color picker than all subsequent times
3. The colour picker is better than it was, but still not perfect
    * I will try and make it better when I learn how to and have time
4. You may use it without the electron-hue-color-picker, and it will retain all functionality, except changing colors