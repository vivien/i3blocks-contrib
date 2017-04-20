# [Script Name](https://github.com/vivien/i3blocks-contrib/tree/master/script_name)

*Screenshot(s) (Cropped), minimum of one. Delete this italic text when posting.*

[![Screenshot](https://i.imgur.com/Ytxua6Z.png)](https://i.imgur.com/Ytxua6Z.png)
[![Screenshot](https://i.imgur.com/tWYjhOl.png)](https://i.imgur.com/tWYjhOl.png)

1 paragraph follows with information on the script and it's design goals. Why was it written? What does it do? DO NOT answer how it is used or works here!

## Dependencies

* i3blocks Version >= 1.5
* Unicode Font Support
* [Font Awesome](https://fortawesome.github.io/Font-Awesome/)
* [boost-libs](http://www.boost.org/)

### Optional

* [python3-feedparser](https://pypi.python.org/pypi/feedparser)

## Installation

This section is allowed and notes anything special required to install and use the script. You SHOULD NOT need this section and may thus delete it. Refer to the [[Installation]] page in the wiki to see how your script can be structured to disregard this section. Again, use of this section is highly discouraged.

## Usage

*Remove any unused fields in the config below. Leave in ONLY fields that must be filled for your script to function (choosing any reasonable default is fine). Avoid modifying any fields that are not critical to your script running successfully (eg. color). Delete this italic text when posting.*

```ini
[script]
#label=
command=script_name.ext -f -l -s
interval=30
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

```
script_name.ext [-f [-l]] [-a] [-g] [-s]
    -f    Force execution
    -l    Leave alone
    -a    Always run
    -g    Use grep instead of internal
    -s    Suppress information
```

This is where everything else should go about the script. Examples would include:
* MUST be run with the `-s` flag for it to work with i3blocks
* SHOULD be run with `interval=30` or less
* Is Pango mandatory? Optional? Unusable?

Or perhaps, a paragraph about how your dependencies work. For example, maybe this script only needs python3-feedparser if the `-f` or `-a` flags are used.

Perhaps you have a paragraph or two about internals of the program itself so that users can make minor configuration changes such as a hard coded colour or design choice without a patch or Github issue.

Another paragraph perhaps about how you could go about filtering the output with another program and a pipe? Explain how the clickable icons in the blocklet work? Any environment variables? This section is similar to a man page for your script, so be through. You get the idea...

### Examples

This is where some handy example usages may be placed (if needed/desired). This section will often not be needed (and thus omitted) but may be used here if it will aid usability.
