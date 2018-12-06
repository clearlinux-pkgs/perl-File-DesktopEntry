#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-DesktopEntry
Version  : 0.22
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-DesktopEntry-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-DesktopEntry-0.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-desktopentry-perl/libfile-desktopentry-perl_0.22-1.debian.tar.xz
Summary  : 'Module to handle .desktop files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-DesktopEntry-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::BaseDir)
BuildRequires : perl(URI::Escape)

%description
# File-DesktopEntry
You can use this module to work with `.desktop` files as specified
by the Freedesktop.org specification.

%package dev
Summary: dev components for the perl-File-DesktopEntry package.
Group: Development
Provides: perl-File-DesktopEntry-devel = %{version}-%{release}

%description dev
dev components for the perl-File-DesktopEntry package.


%package license
Summary: license components for the perl-File-DesktopEntry package.
Group: Default

%description license
license components for the perl-File-DesktopEntry package.


%prep
%setup -q -n File-DesktopEntry-0.22
cd ..
%setup -q -T -D -n File-DesktopEntry-0.22 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-DesktopEntry-0.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-DesktopEntry
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-DesktopEntry/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/File/DesktopEntry.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::DesktopEntry.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-DesktopEntry/deblicense_copyright
