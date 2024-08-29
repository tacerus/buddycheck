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


%bcond_without apparmor
Name:           buddycheck
Version:        1.2
Release:        0
Summary:        Health check
License:        EUPL-1.2
Group:          System/Monitoring
URL:            https://git.com.de/Georg/buddycheck
Source:         %{name}-%{version}.tar.zst
BuildArch:      noarch
%if %{with apparmor}
BuildRequires:  apparmor-rpm-macros
%endif

%description
BuddyCheck is a tool querying the systemd health through Prometheus Node Exporter.

%prep
%autosetup

%build
# Perl script, nothing to build

%install
%make_install PREFIX=%{_prefix} MANDIR=%{_mandir} SYSCONFDIR=%{_sysconfdir}

%if %{with apparmor}
%post
%{apparmor_reload %{_sysconfdir}/apparmor.d/%{name}}
%endif

%files
%license LICENSE
%doc README.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/%{name}
%else
%exclude %dir %{_sysconfdir}/apparmor.d
%exclude %config %{_sysconfdir}/apparmor.d/%{name}
%endif

%changelog
