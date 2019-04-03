# airly

Show air quality in your area

![CAQI](airly.png)

# Dependencies

Python 3

**Packages names in Debian based distros**:
python3

**Packages names in Arch Linux**:
python


# Usage

There are two ways to set up airly blocklet. You able to specify options in
**"Settings"** section inside [airly](airly) file. And if you not allowed to
edit airly file, or if you want to use multiple instances of airly block, you
could make .yml config file for each instance in **~/.config/i3blocks-airly/**
directory.

Now keep in mind, that there are also two ways to specify measurements places.
One way is to specify the installationId which may be obtained from the API or
whe airly.eu widgets.

Another way is to use the place lattitude and longitude and specify them explicitly
in the config file, which would give interpolated measurements.

An apikey is a must and may be obtained by registering an user account on airly.eu

Now add a section to your i3blocks.conf like following:
```INI
[airly]
command=$SCRIPT_DIR/airly #note that this line is optional
interval=600
min_width=CAQI: 99
```

If you want to use instance mechanism of i3blocks, you should make config file
in directory **~/.config/i3blocks-airly/** with following structure:
```YML
apikey: 'xxxx' #get it from airly.eu
# then
installationId: 2222
# or
lat: 10.0000
lng: 10.0000
```

The `apikey` key is mandatory and either `installationId` or `lat&lng` have to be chosen.
The minimal config file is:
```YML
apikey: xxxxxxxxxxxxxxxxx
installationId: 2222
```

When config files is created, add an instance option with name of config file
to your i3blocks.conf. Let's imagine, that we have the
~/.config/i3blocks-airly/home.yml file, then airly section should be:
```ini
[airly]
instance=home
interval=600
min_width=CAQI: 99
```

After configuring blocklet restart your window manager.
New block should appear in the i3bar.
