%define module	Finance-Bank-LaPoste
%define name	perl-%{module}
%define version	4.00
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check your "La Poste" accounts from Perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	perl-devel
Buildrequires:  perl-libwww-perl

Buildarch:	noarch

Requires:	perl(Crypt::SSLeay)

%description
This module provides a read-only interface to the Videoposte online
banking system at <https://www.videoposte.com/>.

The interface of this module is similar to other Finance::Bank modules.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Finance/Bank/*
%{_mandir}/*/*

