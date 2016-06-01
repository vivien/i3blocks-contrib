#####################################
#
#	Created By Thomas MEREL
#	<thomas.merel.44@gmail.com>
#
#####################################

INFO :

	This blocklet is used to control your screen brightness with scroll
	Blocket based on @EliteTK sound manager for i3blocks

DEPENDENCIES :

	xbacklight
	ttf-font-icons
	ttf-font-awesome

MY PERSONNAL I3 BLOCK CONF :

	[brightness]
	align=right
	instance=5
	interval=1
	signal=11
	min_width="  0%"

HOW XBACKLIGHT WORK :

	> xbacklight
	# Return current brightness

	> xbacklight -inc X
	# Increase brightness of X percent

	> xbacklight -dec X
	# Decrease brightness of X percent

HOW MY BLOCKET WORK :

	Place your cursor on the brightness block, scroll up or down for increase or decrease the brightness of your screen

Last Update : 02 may 2016
