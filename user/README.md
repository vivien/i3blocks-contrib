# user

Show current user name.

![](user.png)

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

