Summary:        Fedora Modular release files
Name:           modular-release
Version:        26
Release:        0.1%{?dist}
License:        MIT
Group:          System Environment/Base
URL:            https://pagure.io/fedora-release
Source0:        90-default.preset
Source1:        99-default-disable.preset
Source2:        LICENSE
Source3:        Fedora-Legal-README.txt
Provides:       redhat-release
Provides:       system-release
Provides:       system-release(%{version})

#Requires:       modular-repos(%{version})
BuildArch:      noarch

%description
Fedora release files such as various /etc/ files that define the modular
release.

%prep
cp %{SOURCE2} %{SOURCE3} .

%build


%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/user-preset/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/

install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/


%files
%license LICENSE Fedora-Legal-README.txt
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset

