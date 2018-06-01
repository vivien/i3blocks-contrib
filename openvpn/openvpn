#!/usr/bin/env perl
# Made by Pierre Mavro/Deimosfr <deimos@deimos.fr>
# Minor contribution by Thor K. H. <thor@roht.no>
# Licensed under the terms of the GNU GPL v3, or any later version.
# Version: 0.3

# Usage:
# 1. The configuration name of OpenVPN should be familiar for you (home,work...)
# 2. The device name in your configuration file should be fully named (tun0,tap1...not only tun or tap)
# 3. When you launch one or multiple OpenVPN connexion, be sure the PID file is written in the correct folder (ex: --writepid /run/openvpn/home.pid)

use strict;
use warnings;
use utf8;
use Getopt::Long;

my $openvpn_enabled='/dev/shm/openvpn_i3blocks_enabled';
my $openvpn_disabled='/dev/shm/openvpn_i3blocks_disabled';

# Print output
sub print_output {
    my $ref_pid_files = shift;
    my @pid_files = @$ref_pid_files;
    my $change=0;

    # Total pid files
    my $total_pid = @pid_files;
    if ($total_pid == 0) {
        print "down\n"x2;
        # Delete OpenVPN i3blocks temp files
        if (-f $openvpn_enabled) {
            unlink $openvpn_enabled or die "Can't delete $openvpn_enabled\n";
            # Colorize if VPN has just went down
            print '#FF0000\n';
        }
        unless (-f $openvpn_disabled) {
            open(my $shm, '>', $openvpn_disabled) or die "Can't write $openvpn_disabled\n";
        }
        exit(0);
    }

    # Check if interface device is present
    my $vpn_found=0;
    my $pid;
    my $cmd_line;
    my @config_name;
    my @config_path;
    my $interface;
    my $config_prefix;
    my $current_config_path;
    my $current_config_name;
    foreach (@pid_files) {
        # Get current PID
        $pid=0;
        open(PID, '<', $_);
        while(<PID>) {
            chomp $_;
            $pid = $_;
        }
        close(PID);
        # Check if PID has been found
        if ($pid ==0) {
            print "Can't get PID $_: $!\n";
        }

        # Check if PID is still alive
        $cmd_line='/proc/'.$pid.'/cmdline';
        if (-f $cmd_line) {
            # Get config name
            open(CMD_LINE, '<', $cmd_line);
            while(<CMD_LINE>) {
                chomp $_;
                $config_prefix = "";
                if ($_ =~ /--cd\x{00}(.*?)\x{00}/) {
                    $config_prefix = $1;
                }
                if ($_ =~ /--config\x{00}(.*?\.conf)\x{00}/) {
                    # Get interface from config file
                    $current_config_path = $1;
                    # Remove unwanted escape chars
                    $interface = 'null';
                    # Get configuration name
                    if ($current_config_path =~ /(\w+).conf/) {
                        $current_config_name=$1;
                    } else {
                        $current_config_name='unknown';
                    }

                    $current_config_path = "$config_prefix/$current_config_path";

                    # Get OpenVPN interface device name
                    open(CONFIG, '<', $current_config_path) or die "Can't read config file '$current_config_path': $!\n";
                    while(<CONFIG>) {
                        chomp $_;
                        if ($_ =~ /dev\s+(\w+)/) {
                            $interface=$1;
                            last;
                        }
                    }
                    close(CONFIG);
                    # check if interface exist
                    unless ($interface eq 'null') {
                        if (-d "/sys/class/net/$interface") {
                            push @config_name, $current_config_name;
                            $vpn_found=1;
                            # Write enabled file
                            unless (-f $openvpn_enabled) {
                                open(my $shm, '>', $openvpn_enabled) or die "Can't write $openvpn_enabled\n";
                                $change=1;
                            }
                        }
                    }
                }
            }
            close(CMD_LINE);
        }
    }

    # Check if PID found
    my $names;
    my $short_status;
    if ($vpn_found == 1) {
        $names = join('/', @config_name);
        $short_status='up';
    } else {
        $short_status='down';
        $names = $short_status;
    }

    print "$names\n";
    print "$short_status\n";

    # Print color if there were changes
    print "#00FF00\n" if ($change == 1);

    exit(0);
}

sub check_opts {
    # Vars
    my $pid_file_format=$ENV{PID_FILE_FORMAT} || '/run/openvpn/*.pid';

    # Set options
    GetOptions( "help|h" => \&help,
        "p=s"    => \$pid_file_format);

    my @pid_file=glob $pid_file_format;
    print_output(\@pid_file);
}

sub help {
    print "Usage: openvpn [-p pid_file_format]\n";
    print "-p : format string to glob all pid files (default '/run/openvpn/*.pid)'\n";
    print "Note: devices in configuration file should be named with their number (ex: tun0, tap1)\n";
    exit(1);
}

&check_opts;
