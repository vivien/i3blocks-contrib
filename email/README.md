# email

Show the count of new messages in your
email box using IMAP.
Left button mouse click opens custom URL.

![message](email.png)

# Dependencies

Python 3, [python-keyring](https://pypi.python.org/pypi/keyring) (optional),
gnome-keyring (if pyton-keyring using, also you able to use any other
compatible backend)

**Packages names in Debian based distros**:
python3, python3-keyring, gnome-keyring

**Packages names in Arch Linux**:
python, python-keyring, gnome-keyring


Alternatively you can get python-keyring with
[pip](https://pypi.python.org/pypi/pip):

```shell
$ pip install keyring
```

# Usage

There are two ways to set up email blocklet. You able to specify options in
**"Settings"** section inside [email](email) file. And if you not allowed to
edit email file, or if you want to use multiple instances of email block, you
could make config file for each instance in **~/.config/i3blocks-email/**
directory.

Now keep in mind, that there are also two ways to specify your mailbox password.
One way is to past it between apostrophes in PASS line in blocklet or config
file. **It is not secure and it is recommended for debugging only!**

Another way is to use a system keyring. In this way you should keep PASS empty
as is. To add your password to keyring run:

```shell
$ $SCRIPT_DIR/email --add $USER
```
where $USER is your mailbox login.

**python-keyring and compatible backend should be installed and be in $PATH.**

You also able to delete key with:
```shell
$ $SCRIPT_DIR/email --remove $USER
```


Now add a section to your i3blocks.conf like following:
```INI
[email]
command=$SCRIPT_DIR/email
interval=300
min_width=messages: 99
```

If you want to use instance mechanism of i3blocks, you should make config file
in directory **~/.config/i3blocks-email/** with following structure:
```INI
[MAIL]

HOST: imap.mail_server.com
PORT: 993
USER: my_mailbox@mail_server.com
PASS:
URL: https://www.mail_server.com

```

The [MAIL] header should exist. Any options are optional and replace the same
options inside [email](email).
The minimal config file is:
```INI
[MAIL]

HOST: imap.mail_server.com
USER: my_mailbox@mail_server.com
```

When config files is created, add an instance option with name of config file
to your i3blocks.conf. Let's imagine, that we have the
~/.config/i3blocks-email/my\_mailbox\_config file, then email section should be:
```ini
[email]
command=$SCRIPT_DIR/email
instance=my_mailbox_config
interval=60
min_width=messages: 99
```

After configuring blocklet restart your window manager.
New block should appear in the i3bar.
