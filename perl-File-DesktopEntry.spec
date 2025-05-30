#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-File-DesktopEntry
Version  : 0.22
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-DesktopEntry-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-DesktopEntry-0.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-desktopentry-perl/libfile-desktopentry-perl_0.22-1.debian.tar.xz
Summary  : 'Module to handle .desktop files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-DesktopEntry-license = %{version}-%{release}
Requires: perl-File-DesktopEntry-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::BaseDir)
BuildRequires : perl(URI::Escape)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# File-DesktopEntry
You can use this module to work with `.desktop` files as specified
by the Freedesktop.org specification.

%package dev
Summary: dev components for the perl-File-DesktopEntry package.
Group: Development
Provides: perl-File-DesktopEntry-devel = %{version}-%{release}
Requires: perl-File-DesktopEntry = %{version}-%{release}

%description dev
dev components for the perl-File-DesktopEntry package.


%package license
Summary: license components for the perl-File-DesktopEntry package.
Group: Default

%description license
license components for the perl-File-DesktopEntry package.


%package perl
Summary: perl components for the perl-File-DesktopEntry package.
Group: Default
Requires: perl-File-DesktopEntry = %{version}-%{release}

%description perl
perl components for the perl-File-DesktopEntry package.


%prep
%setup -q -n File-DesktopEntry-0.22
cd %{_builddir}
tar xf %{_sourcedir}/libfile-desktopentry-perl_0.22-1.debian.tar.xz
cd %{_builddir}/File-DesktopEntry-0.22
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-DesktopEntry-0.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-DesktopEntry
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-DesktopEntry/739383159925a8c49f25f28b0fd7210be7dfb3cc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::DesktopEntry.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-DesktopEntry/739383159925a8c49f25f28b0fd7210be7dfb3cc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
