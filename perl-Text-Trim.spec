%define upstream_name    Text-Trim
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Remove leading and/or trailing whitespace from strings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides functions for removing leading and/or trailing
whitespace from strings. It is basically a wrapper around some simple
regexes with a flexible context-based interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 655235
- rebuild for updated spec-helper

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 532720
- update to 1.02

* Tue Dec 22 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 481402
- import perl-Text-Trim


* Tue Dec 22 2009 cpan2dist 1.01-1mdv
- initial mdv release, generated with cpan2dist
