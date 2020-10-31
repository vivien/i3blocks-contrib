# user

Show current user name.

![](user.png)

Set you user name via this command:
`sudo usermod -c "YOUR NAME" $USER`

# Dependencies

* `fontawesome. Not necessary but better install it`

# Config

```
[user]
#label= # Install fontawesome for use this
label=User: 
command=lslogins | grep $USER | awk '{print $5,$NF}'
interval=once
```

