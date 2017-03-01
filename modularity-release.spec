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
Fedora release files such as various /etc/ files that define the modular
release.

%prep
cp %{SOURCE2} %{SOURCE3} .

%build


%install

mkdir -p $RPM_BUILD_ROOT/usr/lib/ \
         $RPM_BUILD_ROOT/etc

# Create fedora-release
echo "Fedora modular release %{version} (%{release_name})" > $RPM_BUILD_ROOT/usr/lib/fedora-release
ln -s ../usr/lib/fedora-release $RPM_BUILD_ROOT/etc/fedora-release

echo "cpe:/o:fedoraproject:fedoramodular:%{version}" > $RPM_BUILD_ROOT/usr/lib/system-release-cpe
ln -s ../usr/lib/system-release-cpe $RPM_BUILD_ROOT/etc/system-release-cpe

# Symlink the -release files
ln -s fedora-release $RPM_BUILD_ROOT/etc/redhat-release
ln -s fedora-release $RPM_BUILD_ROOT/etc/system-release

# Create the os-release file
cat << EOF >>$RPM_BUILD_ROOT/usr/lib/os-release
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

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release $RPM_BUILD_ROOT/etc/os-release


# Create /etc/issue
echo "\S" > $RPM_BUILD_ROOT/usr/lib/issue
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT/usr/lib/issue
echo >> $RPM_BUILD_ROOT/usr/lib/issue
ln -s ../usr/lib/issue $RPM_BUILD_ROOT/etc/issue

# Create /etc/issue.net
echo "\S" > $RPM_BUILD_ROOT/usr/lib/issue.net
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT/usr/lib/issue.net
ln -s ../usr/lib/issue.net $RPM_BUILD_ROOT/etc/issue.net


# Create systemd presets
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/user-preset/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/

install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/


%files
%license LICENSE Fedora-Legal-README.txt
/etc/fedora-release
/etc/issue
/etc/issue.net
/etc/os-release
/etc/redhat-release
/etc/system-release
/etc/system-release-cpe
/usr/lib/fedora-release
/usr/lib/issue
/usr/lib/issue.net
/usr/lib/os-release
/usr/lib/system-release-cpe
%dir /usr/lib/systemd/user-preset/
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset

