# Timewarrior blocklet

The blocklet displays the total time spent on the active taskwarrior task since the start of the day.
If not task is active, it displays nothing.

For maximum enjoyment, add the recheck-signal to any timewarrior aliases you have, e.g.:

`alias wt="timew stop && pkill -RTMIN+10 i3blocks"`

The script is simple.

Check timew is tracking something:

```
timew >/dev/null || exit 0
```

Get current timew tags:

```
tags="$(timew | head -n1 | sed 's/Tracking //g')"
```

Using 'timew sum $tags' does not work because bare-ass shell scripts do degenerate things with quotes.
Please @ me if you find a less ugly solution.

```
total=$(echo "timew sum $tags" | sh | tac | grep -oPm1 ' \d:\d\d')
```

Finally, echo the full-blocklet, the short-blocklet, and 'bright white', with 'exit 0' to show that no background colour will follow.

```
echo $tags ⌛ $total

echo ⚒: $total && exit 0
```

## Oneliner version:

```
command=timew >/dev/null || exit 0 && tags="$(timew | head -n1 | sed 's/Tracking //g')" && total=$(echo "timew sum $tags" | sh | tac | grep -oPm1 ' \d:\d\d') && echo $tags ⌛ $total && echo ⚒: $total && exit 0
```

