# afs

Show usage information for an [AFS](https://en.wikipedia.org/wiki/Andrew_File_System) directory.

![](example.png)

## Setup / Usage

Suggested i3blocks configuration:

```
[afs]
command=$SCRIPT_DIR/afs -c 90
label=AFS
instance=~/afs/
markup=pango
interval=600
```

### Options

```
usage: afs [-h] [-c CRITICAL] [-fg FG_COLOR] [-bg BG_COLOR]

Get AFS quota and usage information.

optional arguments:
  -h, --help            show this help message and exit
  -c CRITICAL, --critical CRITICAL
                        Critical usage percentage. (default: 90)
  -fg FG_COLOR, --fg-color FG_COLOR
                        Foreground color for critical usage. (default:
                        #FF0000)
  -bg BG_COLOR, --bg-color BG_COLOR
                        Background color for critical usage. (default: None)
```

## Dependencies

- `fs` command suite shipped with the AFS client software
- python3

