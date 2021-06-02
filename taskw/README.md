# Taskwarrior active task blocklet

This blocklet shows what task(s) you currently have active in TaskWarrior.
The blocklet will display the description of one of the active tasks
and an indication of how many other active tasks you have.

## Config options

 - `TASKW_MAX_LENGTH` : the number of characters to truncate long task descriptions at
 - `TASKW_NOTASK_MSG` : the text to display if there are no active tasks
 - `TASKW_SORT_URGENCY` : a boolean to determine whether to display the most urgent active task (or the default behaviour which is to display the task which has been active longest).
