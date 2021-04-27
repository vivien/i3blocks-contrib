# brightness

## Description

This small tool listens to file "actual_brightness" modification and reports current brightness percentage. Written in C. It can be used with i3blocks persistent block.

![Screenshot](brightness.png)

## How to build

`make release`

The result executable will be placed into bin directory.

## Config

```
[brightness]
command=./brightness/bin/brightness -a /sys/class/backlight/intel_backlight/actual_brightness -m /sys/class/backlight/intel_backlight/max_brightness
interval=persist
```

## Usage

```
brightness 0.1 - read actual brightness value in non-blocking style.

Usage: brightness [options]
          
          Options:
          -a, --actual_brightness_path  	path to file with actual brightness string
          -m, --max_brightness_path     	path to file with max brightness string
          -h, --help                    	print this help.
          -V, --version                 	print version and exit.

```

## Roadmap

- [x] Connect tool with i3blocks
- [ ] Remove full paths from command arguments. Make it possible to set class or device and parse full path automatically via "/sys/brightness" or "/sys/leds". 
