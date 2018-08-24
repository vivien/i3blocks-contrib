#!/usr/bin/env perl

use strict;
use warnings;
use POSIX qw/strftime/;

my $click   = $ENV{BLOCK_BUTTON} || 0;
my $format  = $ENV{BLOCK_INSTANCE} || $ENV{STRFTIME_FORMAT} || "%H:%M";
my $tz_file = shift || $ENV{TZ_FILE} || "$ENV{HOME}/.tz";
$tz_file = glob($tz_file);
my $default_tz = get_default_tz();

my $tzones = $ENV{TZONES} || '$DEFAULT_TZ';
$tzones =~ s/\$DEFAULT_TZ/$default_tz/g;
my @tz_list = split(/,/, $tzones);
my @tz_labels = split(/,/, $ENV{TZ_LABELS} || "");
if (scalar(@tz_list) != scalar(@tz_labels)) {
    @tz_labels = @tz_list;
}

my $current_tz;
if ($click == 1) {
    $current_tz = get_tz();

    my %tzmap;
    $tzmap{""} = $tz_list[0];
    my $prev = $tz_list[0];
    foreach my $tz (@tz_list) {
        $tzmap{$prev} = $tz;
        $prev = $tz;
    }
    $tzmap{$prev} = $tz_list[0];

    if (exists $tzmap{$current_tz}) {
        set_tz($tzmap{$current_tz});
        $current_tz = $tzmap{$current_tz};
    }
}

# How each timezone will be displayed in the bar.
my %display_map;
for (my $i=0; $i < scalar(@tz_list); $i++) {
    $display_map{$tz_list[$i]} = $tz_labels[$i];
}

if (!defined $current_tz) {
    $current_tz = get_tz();
    set_tz($current_tz);
}
$ENV{TZ} = $current_tz;
my $tz_display = "";
if (!exists $display_map{$ENV{TZ}}) {
    $ENV{TZ} = $tz_list[0];
    set_tz($tz_list[0]);
}
$tz_display = $display_map{$ENV{TZ}};

my $time = strftime($format, localtime());
if ($tz_display eq "") {
    print "$time\n";
} else {
    print "$time ($tz_display)\n";
}

sub get_tz {
    my $current_tz;

    if (-f $tz_file) {
        open my $fh, '<', $tz_file || die "Couldn't open file: $tz_file";
        $current_tz = <$fh>;
        chomp $current_tz;
        close $fh;
    }

    return $current_tz || get_default_tz();
}

sub set_tz {
    my $tz = shift;

    open my $fh, '>', $tz_file || die "Couldn't open file: $tz_file";
    print $fh $tz;
    close $fh;
}

sub get_default_tz {
    my $tz = "Europe/London";

    if (-f "/etc/timezone") {
        open my $fh, '<', "/etc/timezone" || die "Couldn't open file: /etc/timezone";
        $tz = <$fh>;
        chomp $tz;
        close $fh;
    } elsif (-l "/etc/localtime") {
        $tz = readlink "/etc/localtime";
        $tz = (split /zoneinfo\//, $tz)[-1];
    }

    return $tz;
}
