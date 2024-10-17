%define upstream_name	 Finance-Bank-LaPoste
%define upstream_version 7.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check your "La Poste" accounts from Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Graphics::Magick)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(HTML::Form)
BuildRequires:	perl(HTML::Parser)
Requires:	perl(Crypt::SSLeay)
BuildArch:	noarch

%description
This module provides a read-only interface to the Videoposte online
banking system at <https://www.videoposte.com/>.

The interface of this module is similar to other Finance::Bank modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Finance/Bank/*
%{_mandir}/*/*
