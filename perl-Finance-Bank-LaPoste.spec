%define upstream_name	 Finance-Bank-LaPoste
%define upstream_version 7.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Check your "La Poste" accounts from Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:  perl-libwww-perl

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(Crypt::SSLeay)

%description
This module provides a read-only interface to the Videoposte online
banking system at <https://www.videoposte.com/>.

The interface of this module is similar to other Finance::Bank modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
