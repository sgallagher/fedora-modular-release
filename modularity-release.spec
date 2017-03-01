%define release_name Twenty Six
%define dist_version 26
%define bug_version 26

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
Conflicts:      fedora-release

#Requires:       modular-repos(%{version})
BuildArch:      noarch

%description
Fedora release files such as various %{_sysconfdir}/ files that define the modular
release.

%prep
cp %{SOURCE2} %{SOURCE3} .

%build


%install

mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/ \
         $RPM_BUILD_ROOT%{_sysconfdir}

# Create fedora-release
echo "Fedora modular release %{version} (%{release_name})" > $RPM_BUILD_ROOT%{_prefix}/lib/fedora-release
ln -s ..%{_prefix}/lib/fedora-release $RPM_BUILD_ROOT%{_sysconfdir}/fedora-release

echo "cpe:/o:fedoraproject:fedoramodular:%{version}" > $RPM_BUILD_ROOT%{_prefix}/lib/system-release-cpe
ln -s ..%{_prefix}/lib/system-release-cpe $RPM_BUILD_ROOT%{_sysconfdir}/system-release-cpe

# Symlink the -release files
ln -s fedora-release $RPM_BUILD_ROOT%{_sysconfdir}/redhat-release
ln -s fedora-release $RPM_BUILD_ROOT%{_sysconfdir}/system-release

# Create the os-release file
cat << EOF >>$RPM_BUILD_ROOT%{_prefix}/lib/os-release
NAME=Fedora
VERSION="%{dist_version} (%{release_name})"
ID=fedoramodular
VERSION_ID=%{dist_version}
PRETTY_NAME="Fedora Modular %{dist_version} (%{release_name})"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedoramodular:%{dist_version}"
HOME_URL="https://fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{bug_version}
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=%{bug_version}
PRIVACY_POLICY_URL=https://fedoraproject.org/wiki/Legal:PrivacyPolicy
EOF

# Create the symlink for %{_sysconfdir}/os-release
ln -s ..%{_prefix}/lib/os-release $RPM_BUILD_ROOT%{_sysconfdir}/os-release


# Create %{_sysconfdir}/issue
echo "\S" > $RPM_BUILD_ROOT%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT%{_prefix}/lib/issue
echo >> $RPM_BUILD_ROOT%{_prefix}/lib/issue
ln -s ..%{_prefix}/lib/issue $RPM_BUILD_ROOT%{_sysconfdir}/issue

# Create %{_sysconfdir}/issue.net
echo "\S" > $RPM_BUILD_ROOT%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT%{_prefix}/lib/issue.net
ln -s ..%{_prefix}/lib/issue.net $RPM_BUILD_ROOT%{_sysconfdir}/issue.net


# Create systemd presets
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/systemd/user-preset/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/

install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/


%files
%license LICENSE Fedora-Legal-README.txt
%{_sysconfdir}/fedora-release
%{_sysconfdir}/issue
%{_sysconfdir}/issue.net
%{_sysconfdir}/os-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%{_prefix}/lib/fedora-release
%{_prefix}/lib/issue
%{_prefix}/lib/issue.net
%{_prefix}/lib/os-release
%{_prefix}/lib/system-release-cpe
%dir %{_prefix}/lib/systemd/user-preset/
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset

