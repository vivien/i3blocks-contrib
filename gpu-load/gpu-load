#! /usr/bin/perl

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

use strict;
use warnings;
use utf8;
use Getopt::Long;

# default values
my $t_warn = $ENV{T_WARN} || 70;
my $t_crit = $ENV{T_CRIT} || 90;
my $gpu_usage = -1;
my $gpu_mem = -1;
my $gpu_video = -1;
my $gpu_pcie = -1;

sub help {
    print "Usage: gpu-load [-w <warning>] [-c <critical>]\n";
    print "-w <percent>: warning threshold to become amber\n";
    print "-c <percent>: critical threshold to become red\n";
    exit 0;
}

GetOptions("help|h" => \&help,
           "w=i"    => \$t_warn,
           "c=i"    => \$t_crit);

# Get GPU usage from nvidia-settings
open (NVS, 'nvidia-settings -q GPUUtilization -t |') or die;
while (<NVS>) {
    if (/^[a-zA-Z]*=(\d+), [a-zA-Z]*=(\d+), [a-zA-Z]*=(\d+), [a-zA-Z]*=(\d+)$/) {
        $gpu_usage = $1;
	$gpu_mem = $2;
	$gpu_video = $3;
	$gpu_pcie = $4;
        last;
    }
}
close(NVS);

$gpu_usage eq -1 and die 'Can\'t find GPU information';

# Print full_text, short_text
printf "%.0f%% %.0f%% %.0f%% %.0f%%\n", $gpu_usage, $gpu_mem, $gpu_video, $gpu_pcie;
printf "%.0f%%\n", $gpu_usage;

# Print color, if needed
if ($gpu_usage >= $t_crit || $gpu_mem >= $t_crit || $gpu_video >= $t_crit || $gpu_pcie >= $t_crit) {
    print "#FF0000\n";
    exit 33;
} elsif ($gpu_usage >= $t_warn || $gpu_mem >= $t_warn || $gpu_video >= $t_warn || $gpu_pcie >= $t_warn) {
    print "#FFBF00\n";
}

exit 0;
