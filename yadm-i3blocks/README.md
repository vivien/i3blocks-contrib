# yadm-i3blocks
yadm version control status for i3blocks

## About
This module aims to make it easy to see your current yadm's status in the i3blocks' status bar.
Yadm Yet Another Dotfiles Manager. For this reson, it's helpful to make sure it's always up to date.

## Requirements
- i3blocks
- [yadm](https://yadm.io/)
    - [Or their GitHub](https://github.com/TheLocehiliosaan/yadm)
    
## Installation
Just add these lines to your i3blocks' configuration file:


    [dotfiles]
    command=~/.config/i3blocks/scripts/dotfiles
    interval=1
