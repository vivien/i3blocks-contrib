# afs

Show usage information for an [AFS](https://en.wikipedia.org/wiki/Andrew_File_System) directory.

![](example.png)

## Setup / Usage

Suggested i3blocks configuration:

```
[afs]
command=$SCRIPT_DIR/afs
instance=~/afs/
markup=pango
interval=600
LABEL=AFS 
#CRITICAL=90
#CRIT_FG_COLOR=#FF0000
#CRIT_BG_COLOR=
```

## Dependencies

- `fs` command suite shipped with the AFS client software
- python3

