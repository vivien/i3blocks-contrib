# [Example Blocklet](https://github.com/vivien/i3blocks-contrib/tree/master/example_blocklet)

*This README.md is an example README for your own blocklet during submission. Feel free to copy it as a template. However, delete ALL italics text in this example before submutting a pull request.*

*Screenshot(s) (Cropped), minimum of one.*

[![Screenshot](https://i.imgur.com/RMqNV9K.png)](https://i.imgur.com/RMqNV9K.png)
[![Screenshot](https://i.imgur.com/CesVFaB.png)](https://i.imgur.com/CesVFaB.png)
[![Screenshot](https://i.imgur.com/S0bTkH4.png)](https://i.imgur.com/S0bTkH4.png)
[![Screenshot](https://i.imgur.com/0ImiyE9.png)](https://i.imgur.com/0ImiyE9.png)

*1 paragraph follows with information on the script and it's design goals. Why was it written? What does it do? DO NOT answer how it is used or works here!*

This is an example blocklet to get you started writing your own blocklets. It's functionality is quite useless but neatly demonstrates the interfaces both to and from i3blocks as succinctly as possible. Should you have any questions or comments, please open an issue and our community of developers will be more than happy to help you.

## Dependencies

* i3blocks Version >= 1.4

### Optional

*This section may be deleted if you have no optional dependancies.*

* [Font Awesome](https://fortawesome.github.io/Font-Awesome/) Version >= 4.5
* Pango

## Installation

*This section is allowed and notes anything special required to install and use the script. You SHOULD NOT need this section and may thus delete it. Refer to the [Installation](https://github.com/vivien/i3blocks-contrib/wiki/Installation) page in the wiki to see how your script can be structured to disregard this section. Again, use of this section is highly discouraged.*

## Usage

*Remove any unused fields in the config below. Leave in ONLY fields that must be filled for your script to function (choosing any reasonable default is fine). Avoid modifying any fields that are not critical to your script running successfully (eg. color).*

```ini
[script]
#label=
command=example_blocklet
interval=3
#signal=
#full_text=
#short_text=
#color=
#min_width=
#align=
#name=
#instance=
#urgent=
#separator=
#separator_block_width=
#markup=
#format=
```

*Below here is your man page. Add anything and everything you need.*

```
example_blocklet [options]
    -p    Demonstrate Pango functionality
    -f    Demonstrate FontAwesome functionality
```

This blocklet is a useless yet fun script to start you on your way to writing your own blocklets. It is fully self documented and easy to follow. It has been written in Bash to be as familiar to as many users as possible. Don't feel limited to writing blocklets in shell script though, experiment with any language you want.

Happy hacking!

### Examples

*This is where some handy example usages may be placed (if needed/desired). This section will often not be needed (and thus omitted) but may be used here if it will aid usability.*
