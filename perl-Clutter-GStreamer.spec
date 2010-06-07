#
# TODO:
# - Update source and url when approved on CPAN

%bcond_without	tests		# do not perform "make test"
%include	/usr/lib/rpm/macros.perl

%define	pdir	Clutter
%define pnam	GStreamer
%define ver	0.100
%define rel	4
Summary:	Integration between GStreamer and Clutter
Name:		perl-Clutter-GStreamer
Version:	%{ver}.%{rel}
Release:	2
License:	perl, lgpl
Group:		Development/Languages/Perl
Source0:	http://www.lyricue.org/archive/libclutter-gstreamer-perl_%{ver}-%{rel}.tar.gz
# Source0-md5:	b5aee73b996a5abe0c601aee06708722
URL:		http://www.clutter-project.org/
BuildRequires:	clutter-gst-devel
BuildRequires:	perl-Clutter
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cairo >= 1.000
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib >= 1.220
BuildRequires:	perl-Pango >= 1.140
%endif
Requires:	clutter-gst
Requires:	perl-Clutter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter is a GObject based library for creating fast, visually rich
graphical user interfaces. It is intended for creating single window
heavily stylised applications such as media box UI's, presentations or
kiosk style programs in preference to regular 'desktop' style
applications.

%prep
%setup -q -n %{name}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes NEWS README
%dir %{perl_vendorarch}/%{pdir}/%{pnam}/
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%{perl_vendorarch}/%{pdir}/%{pnam}.pod
%{perl_vendorarch}/%{pdir}/%{pnam}/*.pod
%{perl_vendorarch}/%{pdir}/%{pnam}/Install
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{_mandir}/man3/*
