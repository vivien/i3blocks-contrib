# Github

Shows Github notifications and adds a shortcut to access your notifications. It uses [Hub](https://github.com/github/hub) for api interactions and for an API oauth token.

# Dependencies

- [Hub](https://github.com/github/hub)
- [Font Awesome](https://fontawesome.com) for the Github icon.

# Usage

Clicking the Github icon will open Github's notifications panel.

# Config

```ini
[github]
command=$SCRIPT_DIR/github/github
interval=60
format=json
markup=pango
```
