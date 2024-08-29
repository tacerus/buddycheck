# Makefile for BuddyCheck
#
# Copyright 2024, Georg Pfuetzenreuter <mail@georg-pfuetzenreuter.net>
#
# Licensed under the EUPL, Version 1.2 or - as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence").
# You may not use this work except in compliance with the Licence.
# An English copy of the Licence is shipped in a file called LICENSE along with this applications source code.
# You may obtain copies of the Licence in any of the official languages at https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12.

PREFIX=/usr/local
BINDIR=$(PREFIX)/bin
MANDIR=$(PREFIX)/man

usage:
	@echo 'Available targets: "install", "uninstall"'

install:
	install -d $(DESTDIR)$(BINDIR) $(DESTDIR)$(MANDIR)/man1
	install buddycheck.pl $(DESTDIR)$(BINDIR)/buddycheck
	pod2man buddycheck.1 > $(DESTDIR)$(MANDIR)/man1/buddycheck.1

uninstall:
	rm $(DESTDIR)$(BINDIR)/buddycheck
	rm $(DESTDIR)$(MANDIR)/man1/buddycheck.1