#!/usr/bin/perl
# Return whether a system is healthy according to systemd by querying
# a Prometheus Node Exporter with enabled systemd collector running on it
#
# Copyright 2024, Georg Pfuetzenreuter <mail@georg-pfuetzenreuter.net>
#
# Licensed under the EUPL, Version 1.2 or - as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence").
# You may not use this work except in compliance with the Licence.
# An English copy of the Licence is shipped in a file called LICENSE along with this applications source code.
# You may obtain copies of the Licence in any of the official languages at https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12.

use 5.26.0;

use HTTP::Tiny;

my $buddy = $ENV{'BUDDYCHECK_HOST'};
	die "Please set BUDDYCHECK_HOST\n" unless $buddy;
my $port = $ENV{'BUDDYCHECK_PORT'} || 9100;

my $response = HTTP::Tiny->new->get('http://' . $buddy . ':' . $port . '/metrics');
	die "HTTP request failed\n" unless $response->{success};

say "$response->{protocol} $response->{status} $response->{reason}" unless $response->{status} == 200;

# match any of the following:
#  node_systemd_system_running 0
#  node_systemd_system_running 1
#  node_systemd_system_running{label="value", ...} 0
#  node_systemd_system_running{label="value", ...} 1
$response->{content} =~ /^node_systemd_system_running(?:\{.*\})?\s([01])/m;

if ($1 == 1) {
	say "Buddy is healthy"
} else {
	say "Buddy is sick";
	exit 125
}
