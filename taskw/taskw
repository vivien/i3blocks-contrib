#!/usr/bin/env python3

"""Extracts information from taskwarrior and timewarrior to display in i3block."""

# This is taskw.py v0.3.1

import subprocess
import json
import os
import re


# config options code


def _default(name, default="", arg_type=str):
    """
    Set a parameter based on OS variable.

    Fix the argument type and fall back on given default.

    """
    val = default
    if name in os.environ:
        val = os.environ[name]
    return arg_type(val)


def _strbool(s):
    """Return True if argument is t,T,true,TRUE etc."""
    return s.lower() in ["t", "true", "1"]


# I don't know who originally wrote these functions,
# but many of the python blocklets in i3blocks-contrib use it.

# arch-update added this code on 25 March 2018 and as far as I can tell
# this was the earliest use.


maxlen = _default("TASKW_MAX_LENGTH", default=35, arg_type=int)
notask_msg = _default("TASKW_NOTASK_MSG", default="No Task", arg_type=str)
urgency_tf = _default("TASKW_SORT_URGENCY", default="f", arg_type=_strbool)
taskw_tf = _default("TASKW_TF", default="t", arg_type=_strbool)
timew_tf = _default("TIMEW_TF", default="f", arg_type=_strbool)
pending_tasks_tf = _default("TASKW_PENDING_TF", default="f", arg_type=_strbool)
timew_desc_override = _default("TIMEW_DESC_OVERRIDE", default="f", arg_type=_strbool)
main_filter = _default("TASKW_MAIN_FILTER", default="+ACTIVE", arg_type=str)

# Set timew_tf to true if the override is set.
if timew_desc_override:
    timew_tf = True

##############################
# TESTING TESTING TESTING

# taskw_tf = False
# timew_tf = True
# timew_desc_override = True
# pending_tasks_tf = True
# notask_msg = "~No Task~"
##############################

# text output helper functions


def shorten(string, maxlen=maxlen):
    """Shorten a string to maxlen characters or fewer."""
    if len(string) <= maxlen:
        return string
    else:
        return string[: maxlen - 3] + "..."


# taskw functions


def get_taskw_json(filter_string):
    """Take a taskw filter and returns the json output for task export."""
    return json.loads(
        subprocess.check_output("task " + filter_string + " export", shell=True)
    )


def sort_taskw_info(taskw_json):
    """
    Return task description to display plus number of tasks.

    Take json output from taskw and return the correct task description
    to display and also the number of tasks matching the filter.
    """
    max_urg = 0
    if len(taskw_json) > 0:
        if urgency_tf:
            for i in range(len(taskw_json)):
                if taskw_json[i]["urgency"] > taskw_json[max_urg]["urgency"]:
                    max_urg = i
        return taskw_json[max_urg]["description"], len(taskw_json)
    else:
        return notask_msg, 0


def get_taskw_info(taskw_filter=main_filter):
    """Take a filter and return a task description and number of tasks."""
    j = get_taskw_json(taskw_filter)
    return sort_taskw_info(j)


def export_pending():
    """Return number of taskw pending tasks."""
    return len(get_taskw_json("+PENDING"))


# timew functions


def get_timew_bytes(dom_string):
    """Return byte output from calling timew."""
    try:
        out = subprocess.check_output("timew get " + dom_string, shell=True)
    except subprocess.CalledProcessError:
        out = b""
    return out


def decode_timew_bytes(in_bytes):
    """
    Take timew byte input and return string.

    This function also strips the trailing newline.
    """
    to_string = in_bytes.decode("utf-8")[:-1]
    return to_string


def get_timew_string(dom_string):
    """Return string decoded output from calling timew with dom_string."""
    in_string = get_timew_bytes(dom_string)
    return decode_timew_bytes(in_string)


def get_timew_active():
    """Return True if timew has active tracking."""
    return b"1" in get_timew_bytes("dom.active")


def export_timew_description():
    """
    Extract description from timew output.

    Actually extracts first tag.

    """
    timew_txt = get_timew_string("dom.active.tag.1")
    return timew_txt if get_timew_active() else notask_msg


def pad_time(s):
    """Add '0' to number if necessary."""
    return s if len(s) == 2 else "0" + s


def extract_time(delimiter, input_string):
    """Extract number of hours|minutes|seconds from timew output."""
    match_list = re.findall(r"\d?\d" + delimiter, input_string)
    return pad_time(match_list[0][:-1]) if len(match_list) > 0 else "00"


def translate_timew_string(timew_in_str):
    """Turn timew output time into duration in HH:MM format."""
    duration_hrs = extract_time("H", timew_in_str)
    duration_mins = extract_time("M", timew_in_str)
    return duration_hrs + ":" + duration_mins


def main():
    """Return string to display based on params."""
    task_desc = ""
    task_append = ""
    timew_duration = ""
    pending_text = ""
    if taskw_tf:
        descr, task_num = get_taskw_info()
        task_desc = shorten(descr)
        if task_num > 1:
            task_append = " + " + str(task_num - 1)

    if timew_tf:
        get_string = get_timew_string("dom.active.duration")
        timew_duration = (
            translate_timew_string(get_string) + " " if get_timew_active() else ""
        )

    if timew_desc_override or not taskw_tf:
        task_desc = shorten(export_timew_description())

    if pending_tasks_tf:
        pending_text = f" [{export_pending()}]"

    bar_text = timew_duration + task_desc + task_append + pending_text
    return bar_text


if __name__ == "__main__":
    print(main())
