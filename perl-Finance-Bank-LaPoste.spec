%define upstream_name	 Finance-Bank-LaPoste
%define upstream_version 7.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 7.07
Release:	1

Summary:	Check your "La Poste" accounts from Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/P/PI/PIXEL/Finance-Bank-LaPoste-7.07.tar.gz

BuildRequires:	perl-devel
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

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 7.50.0-1mdv2011.0
+ Revision: 662489
- update to new version 7.05

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 7.40.0-1
+ Revision: 646334
- update to new version 7.04

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 7.30.0-1mdv2011.0
+ Revision: 595973
- update to new version 7.03

* Sat Nov 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 7.20.0-1mdv2011.0
+ Revision: 467871
- update to 7.02

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 7.10.0-1mdv2010.1
+ Revision: 461280
- update to 7.01

* Thu Oct 29 2009 Olivier Blin <oblin@mandriva.com> 7.00-1mdv2010.0
+ Revision: 460181
- 7.00 (fix connecting with latest authentication scheme)

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.00-1mdv2010.0
+ Revision: 389776
- update to new version 6.00

* Wed Nov 05 2008 Pixel <pixel@mandriva.com> 5.00-1mdv2009.1
+ Revision: 299988
- 5.00: adapt to new labanquepostale.fr architecture (rt.cpan.org#40635)

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 4.00-2mdv2009.0
+ Revision: 268511
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.00-1mdv2009.0
+ Revision: 194853
- update to new version 4.00

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 25 2007 Pixel <pixel@mandriva.com> 3.00-1mdv2008.0
+ Revision: 43962
- new release, 3.00 (adapt to new www.videoposte.com architecture)


* Mon Aug 14 2006 Pixel <pixel@mandriva.com> 2.00-1mdv2007.0
- new release

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-2mdk
- Fix BuildRequires

* Tue Sep 20 2005 Pixel <pixel@mandriva.com> 1.03-1mdk
- new release (handle delayed-debit credit card pseudo account)

* Thu Feb 17 2005 Pixel <pixel@mandrakesoft.com> 1.02-1mdk
- new release

* Sat Jan 01 2005 Pixel <pixel@mandrakesoft.com> 1.01-1mdk
- new release

* Thu Jul 08 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.00-1mdk
- 1.00

* Thu Jan 08 2004 Pixel <pixel@mandrakesoft.com> 0.02-1mdk
- new release: internal change (the Finance::Bank::LaPoste::Statement hash now contains the "year")

* Wed Oct 08 2003 Pixel <pixel@mandrakesoft.com> 0.01-1mdk
- initial release


