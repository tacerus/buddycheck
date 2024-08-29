#
# spec file for package buddycheck
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Georg Pfuetzenreuter
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           buddycheck
Version:        1
Release:        0
Summary:        Health check
License:        EUPL-1.2
URL:            https://git.com.de/Georg/buddycheck
Source:         %{name}-%{version}.tar.zst
BuildRequires:  pod2man

%description
BuddyCheck is a tool querying the systemd health through Prometheus Node Exporter.

%prep
%autosetup

%build
# Perl script, nothing to build

%install
%make_install

%files
%license LICENSE
%doc README.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog

