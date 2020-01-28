# mouse switch

General purpose blocklet - run different commands depending of with which mouse button clicks it 
CMDx        command to run on button click x
CMDxIND    what to display on the blocklet
CMDxCOLOR  optional color
![](systemctl.png)
CMD0IND is the initial state
I use it for keyboard layout switching and indicating which one is set

# Config

```
[mouse_switch]
command=$HOME/mouse_switch

min_width=WIDTH
CMD0IND=none

CMD1=abeep -l 1000 -r 1 &
CMD1IND=beep_1
CMD1COLOR=#FF0000

CMD2=abeep -l 1000 -r 2 &
CMD2IND=beep_2
CMD2COLOR=#00FF00

CMD3=abeep -l 1000 -r 3 &
CMD3IND=beep_3
CMD3COLOR=#0000FF

instance=layout
interval=once
markup=pango
```
