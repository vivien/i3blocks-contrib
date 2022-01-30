#!/usr/bin/env python3

import dbus
import sys

def progressBar(perc : float):
    char = ["░", "▒", "█"]
    bar = char[2] * int(perc / 0.2)
    if perc >= 0.99:
        return bar + char[2]
    bar += char[1]
    while len(bar) != 5:
        bar += char[0]
    return bar

def main():
    bus = dbus.SessionBus()
    proxy = bus.get_object('org.mpris.MediaPlayer2.spotifyd','/org/mpris/MediaPlayer2')

    properties_manager = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties')

    if properties_manager:

        if len(sys.argv) > 1:
            if sys.argv[1] == "1":
                dbus.Interface(proxy, 'org.mpris.MediaPlayer2.Player').PlayPause()

        status = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
        if status == "Playing" : status = " "
        else : status = " "

        current = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Position')

        data = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        length = data["mpris:length"]
        title = data["xesam:title"]

        perc = current / length
        progress = progressBar(perc)
        bar = f" [ {title} ]  {status} {progress}"
        print(bar)

if __name__ == "__main__":
    main()
