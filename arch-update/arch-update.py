#!/usr/bin/env python3
#
# Copyright (C) 2017 Marcel Patzwahl
# Licensed under the terms of the GNU GPL v3 only.
#
# i3blocks blocklet script to see the available updates of pacman and the AUR
import subprocess
from subprocess import check_output
import argparse
import re

class AURHelperNotSupportedError(Exception):
    pass

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
        help='Include AUR packages and specify which AUR helper you use. '
        'Attn: Yaourt and yay are supported and must be installed'
    )
    parser.add_argument(
        '-q',
        '--quiet',
        action = 'store_true',
        help = 'Do not produce output when system is up to date'
    )
    parser.add_argument(
        '-w',
        '--watch',
        nargs='*',
        default=[],
        help='Explicitly watch for specified packages. '
        'Listed elements are treated as regular expressions for matching.'
    )
    return parser.parse_args()


def get_updates():
    output = check_output(['checkupdates']).decode('utf-8')
    if not output:
        return []

    updates = [line.split(' ')[0]
               for line in output.split('\n')
               if line]

    return updates

def run_aur_helper(aur_helper):
    # assume aur_helper is yaourt or yay
    # both work in the same way (use same flags and
    # exit with 1 if there are no updates available)

    if aur_helper not in ['yaourt', 'yay']:
        raise AURHelperNotSupportedError(aur_helper + ' is not a recognised or supported AUR helper!')
    try:
        output = check_output([aur_helper, '-Qua']).decode('utf-8')
    except subprocess.CalledProcessError as exc:
        # exits with 1 and no output if no updates are available.
        # we ignore this case and go on
        if not (exc.returncode == 1 and not exc.output):
            raise exc
    if output:
        return output
    else:
        return []


def get_aur_updates(aur_helper):
    output = run_aur_helper(aur_helper)

    if output == []:
        return output

    aur_updates = [line.split(' ')[0]
                   for line in output.split('\n')
                   if line.startswith('aur/')]

    return aur_updates


def matching_updates(updates, watch_list):
    matches = set()
    for u in updates:
        for w in watch_list:
            if re.match(w, u):
                matches.add(u)

    return matches


message = "<span color='{0}'>{1}</span>"
args = create_argparse()

updates = get_updates()
if args.aur is not None:
    updates += get_aur_updates(args.aur)

update_count = len(updates)
if update_count > 0:
    info = str(update_count) + ' updates available'
    matches = matching_updates(updates, args.watch)
    if matches:
        info += ' [{0}]'.format(', '.join(matches))
    print(message.format(args.updates_available_color, info))
elif not args.quiet:
    print(message.format(args.base_color, 'system up to date'))
