# Eyedropper

Simple and convenient tool to identify the hex value of any color on the screen. Simply click on the icon:

![](eyedropper_startup.png)

Your mouse will become a crosshair. Click on any color you desire and both the color and the hex value will be displayed.

![](eyedropper_example1.png)
![](eyedropper_example2.png)
![](eyedropper_example3.png)

Should you select the color of your bar, you will not be able to see the icon (as the icon and the bar are the same color), but you will still be able to read the hex value
![](eyedropper_same_color.png)

### Dependencies

1. Ensure **grabc** is installed. For debian:

```
$ sudo apt-get install grabc
```

For more information, visit [muquit/grabc](https://github.com/muquit/grabc)

2. [fontawesome](https://github.com/FortAwesome/Font-Awesome)

# Installation

1. Copy script to your directory of choice
2. Give it execution permission (`chmod +x eyedropper`)
3. Add the following blocklet to your i3blocks.conf:

### Configuring i3blocks

```ini
[eyedropper]
command=$SCRIPT_DIR/eyedropper
full_text=<span foreground="#ffffff"></span>
instance=#ffffff
markup=pango
```

- Change the "foreground" value in "full_text" to change the color of the initial eyedropper icon
- Change the "instance" value to change the color of the hex value displayed

### Sample Look

![](eyedropper_sample.png)
