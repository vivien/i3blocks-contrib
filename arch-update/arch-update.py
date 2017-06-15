#!/usr/bin/env python3
#
# Copyright (C) 2017 Marcel Patzwahl
# Licensed under the terms of the GNU GPL v3 only.
#
# i3blocks blocklet script to see the available updates of pacman and the AUR
import subprocess
from subprocess import check_output
import argparse


def create_argparse():
    parser = argparse.ArgumentParser(description='Check for pacman updates')
    parser.add_argument(
        '-b',
        '--base_color',
        default='green',
        help='base color of the output(default=green)'
    )
    parser.add_argument(
        '-u',
        '--updates_available_color',
        default='yellow',
        help='color of the output, when updates are available(default=yellow)'
    )
    parser.add_argument(
        '-a',
        '--aur',
        action='store_true',
        help='Include AUR packages. Attn: Yaourt must be installed'
    )
    return parser.parse_args()


def get_update_count():
    output = check_output(['checkupdates']).decode('utf-8')
    if not output:
        return 0

    updates = [line
               for line in output.split('\n')
               if line]

    return len(updates)


def get_aur_update_count():
    output = ''
    try:
        output = check_output(['yaourt', '-Qua']).decode('utf-8')
    except subprocess.CalledProcessError as exc:
        # yaourt exits with 1 and no output if no updates are available.
        # we ignore this case and go on
        if not (exc.returncode == 1 and not exc.output):
            raise exc
    if not output:
        return 0

    aur_updates = [line
                   for line in output.split('\n')
                   if line.startswith('aur/')]

    return len(aur_updates)


message = "<span color='{0}'>{1}</span>"
args = create_argparse()

update_count = get_update_count()

if args.aur:
    update_count += get_aur_update_count()
if update_count == 0:
    print(message.format(args.base_color, 'system up to date'))
else:
    info = str(update_count) + ' updates available'
    print(message.format(args.updates_available_color, info))
