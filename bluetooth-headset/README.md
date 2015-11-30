# bluetooth-headset

bluetooth-headset is an i3block script able to display bluetooth headset
status. It also handles (dis)connection when the user clicks it.

# Dependencies

* Working bluetooth configuration - distribution dependent
* Your user should be able to `sudo` commands
* Pulse Audio and its pavucontrol utility
* [Font Awesome](https://fortawesome.github.io/Font-Awesome/)

# Usage

Before using this script, please ensure your bluetooth configuration is
working and your device is paired. Also, you should get your device's ID.
You could have it displayed by launchincg bluetoothctl.

For example, here is a sample output when launching bluetoothctl in a
terminal, where the privata date was edited-out:

  ```
  $ bluetoothctl
  [NEW] Controller 99:99:99:99:99:99 your_host [default]
  [NEW] Device xx:xx:xx:xx:xx:xx MDR-ZX330BT
  [NEW] Device 99:99:99:99:99:99 deviceX
  # quit
  $
  ```

In this output, the BT headset is the one named MDR-WX330BT. Please refer to
your product's documentation for the actual device name. You should save or
write down the xx:xx....:xx digit series.

Now open the i3blocks config in your favourite text editor and add this:

  ```
  [headset]
  interval=60
  command= ~/.config/i3blocks/i3blocks-btheadset "xx:xx:xx:xx:xx:xx"
  ```

  ```
  i3blocks-headset HEADSET_ID
      HEADSET_ID is the bluetooth ID of your headset.
  ```

Reload i3 configuration and you now should see right away a new block showing
a small headset. It's green if the device is connected or neutral (that is,
your i3blocks default color) if the headset is not connected. Click it to
change the status of the headset connection. Please allow for several seconds when
clicking because of the bluettooth latency.

If you see a small rectangle instead of the headset icon, please adjust your
font to get one that actually has the symbol. A good choice would be _terminus_
font.

# Options

The main blocklet script is called `i3blocks-btheadset`. This script
only accepts the headset ID as described above. Behind the scenes, it calls
another script, in the same directory, called `btheadset.sh`.

The `btheadset.sh` is provided separately because it's handy to have it for
situations shere you'd like to handle your bluetooth headset from the command
line. This script can be invoked like this:

  ```
  $ ./btheadset.sh on|off|status [HEADSET_ID]
  ```

The first parameter is the command you want it to perform:

* *on* will connect the headset (it must have been previously paired by you)
* *off* will disconnect the headset so you could connect it to another device
* *status* will display the connected or disconnected status

If you want to avoid typing the HEADSET_ID each time, then edit this script
and insert the device ID on the line reading:

  ```
  HEADSET_ID=""
  ```

Put the device ID between the double colons, then save the file. Yous should
now be able to invoke the script without specifying this id. Test it on the
command line and check it successfully handles your bluetooth headset
connection status.

Another thing that may be adjusted into this script is the Pulse Audio profile
used by the headset. By default, the "High Fidelity" profile is automatically
selected when the device is connected. If you'd rather use another profile,
then change the line reading:

  ```
  HEADSET_PROFILE="a2dp_sink"
  ```

Please refer to the Pulse Audio documentation for the correct string to be
used here. Alternatively, you could change it in the `pavucontrol` utility
then use this to see what's the needed string:

  ```
  $ pacmd list-cards # the search through the output to see the profile string
  ```
