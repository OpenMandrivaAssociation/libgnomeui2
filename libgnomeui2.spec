%define api_version	2
%define lib_major	0
%define pkgname		libgnomeui

%define libname		%mklibname gnomeui %{api_version} %{lib_major}
%define develname	%mklibname -d gnomeui %{api_version}

Summary:	Main GNOME libraries
Name:		%{pkgname}%{api_version}
Version:	2.24.5
Release:	19
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
# (fc) 2.22.1-2mdv link with math library
Patch0:		libgnomeui-2.22.1-floor.patch

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gtk-doc >= 0.9
BuildRequires:	pkgconfig(gconf-2.0) >= 1.1.11
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gnome-keyring-1) >= 0.4
BuildRequires:	pkgconfig(gnome-vfs-2.0) >= 2.7.3
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libbonoboui-2.0) >= 2.13.1
BuildRequires:	pkgconfig(libglade-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libgnome-2.0) >= 2.13.7
BuildRequires:	pkgconfig(libgnomecanvas-2.0) >= 2.0.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.20
BuildRequires:	pkgconfig(pango) >= 1.1.2

Requires:	gnome-icon-theme

%description
Data files for the GNOME UI library such as translations.

%package -n %{libname}
Summary:	GNOME libraries
Group:		%{group}

%description -n %{libname}
GNOME library contains extra widgets to let your 
GNOME applications really shine

%package -n %{develname}
Summary:	Development libraries, include files for GNOME
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname -d gnomeui 2 0} < 2.24.5-5

%description -n %{develname}
Development library, headers files and documentation needed in order 
to develop applications using the GNOME library.

%prep
%setup -qn %{pkgname}-%{version}
%autopatch -p1

#needed by patch0
autoreconf -fi

%build
%configure \
	--enable-compile-warnings=no

%make_build

%install
%make_install

%find_lang %{pkgname}-2.0

%files -f %{pkgname}-2.0.lang
%doc AUTHORS NEWS README
%{_libdir}/libglade/2.0/*.so
%{_datadir}/pixmaps/*

%files -n %{libname}
%{_libdir}/libgnomeui-2.so.0*

%files -n %{develname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

%changelog
* Thu Nov 17 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.24.5-4
+ Revision: 731450
- rebuild
- cleaned up spec
- removed defattr
- removed .la files
- removed clean section
- disabled static build
- removed old ldconfig scriptlets
- converted RPM_BUILD_ROOT to buildroot
- switched to autopatch -p1 macros
- changed macro from libnamedev to develname
- fixed devel pkg description & summary
- removed reqs for devel pkgs in devel pkg
- removed reqs for libs in lib pkg
- removed extra devel pkg provide
- removed req for main pkg by devel & lib pkg
- converted BRs to pkgconfig provides
- removed mkrel
- removed  BuildRoot

* Mon Sep 19 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.5-3
+ Revision: 700350
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.24.5-2
+ Revision: 666077
- mass rebuild

* Mon Jan 31 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.5-1
+ Revision: 634559
- update to new version 2.24.5

* Tue Dec 14 2010 Funda Wang <fwang@mandriva.org> 2.24.4-2mdv2011.0
+ Revision: 621679
- rebuild for new popt

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.4-1mdv2011.0
+ Revision: 581460
- update to new version 2.24.4

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.3-1mdv2010.1
+ Revision: 529731
- update to new version 2.24.3

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 2.24.2-4mdv2010.1
+ Revision: 506914
- rebuild for new popt

* Wed Dec 30 2009 Pascal Terjan <pterjan@mandriva.org> 2.24.2-3mdv2010.1
+ Revision: 483997
- Update BuildRequires

* Thu Dec 10 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.24.2-2mdv2010.1
+ Revision: 476023
- fix compilation with new libtool

* Tue Sep 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.2-1mdv2010.0
+ Revision: 447513
- update to new version 2.24.2

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.24.1-2mdv2010.0
+ Revision: 425558
- rebuild

* Fri Mar 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 349840
- update to new version 2.24.1

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286814
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273732
- new version
- drop patch 1

* Mon Jul 14 2008 Adam Williamson <awilliamson@mandriva.org> 2.23.4-2mdv2009.0
+ Revision: 234430
- add gtype.patch from upstream SVN: use gtype instead of gtktype (fixes
  brasero build)

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 230969
- new version
- drop patch 1
- update license
- fix buildrequires
- update file list

* Thu Jun 12 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.1-2mdv2009.0
+ Revision: 218404
- Patch0: add missing link to math lib
- Patch1 (SVN): various bug fixes

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version
    - drop patch

* Tue Apr 01 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.01-2mdv2008.1
+ Revision: 191442
- Patch0 (SVN): fix thumbnail over gio (GNOME bug #517276)

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.01-1mdv2008.1
+ Revision: 183601
- new version
- new version

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.93-1mdv2008.1
+ Revision: 183022
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175047
- new version

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165847
- new version
- update deps

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159216
- new version

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152137
- new version
- drop the patch
- update file list

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1.1-1mdv2008.1
+ Revision: 99887
- new version

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98396
- new version
- drop patch 1

* Wed Oct 03 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-2mdv2008.0
+ Revision: 94957
- Patch1 (SVN): improve volume/drive list consistency

* Wed Sep 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 90885
- new version

* Tue Aug 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.1-3mdv2008.0
+ Revision: 59905
- Remove patches 3, 4, 5, no longer needed with switch to XDG user dirs

* Tue Jul 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-2mdv2008.0
+ Revision: 57247
- new devel name

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-1mdv2008.0
+ Revision: 56583
- new version
- update file list

* Tue Jun 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.0
+ Revision: 41288
- new version


* Wed Mar 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2007.1
+ Revision: 143330
- new version

* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 141790
- new version
- readd changelog

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Tue Feb 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126222
- new version

* Wed Feb 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-2mdv2007.1
+ Revision: 120753
- bump

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 119020
- new version

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 111949
- new version

* Tue Jan 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.1-1mdv2007.1
+ Revision: 106279
- new version

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.0-1mdv2007.1
+ Revision: 90675
- new version

* Thu Nov 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-6mdv2007.1
+ Revision: 89088
- rebuild

* Wed Nov 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-5mdv2007.1
+ Revision: 88343
- rebuild

* Tue Oct 17 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.16.1-4mdv2007.1
+ Revision: 65486
- add BuildRequires: libsm-devel - for gnome-session

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-3mdv2006.0
+ Revision: 63758
- rebuild
- fix patch 5
- unzip patches
- Import libgnomeui2

* Fri Oct 06 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- drop patch 6
- rediff patch 5
- New version 2.16.1

* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-3mdv2007.0
- Patch6 (CVS): fix file-chooser deadlock

* Fri Sep 08 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-2mdv2007.0
- Update patches 3, 4, 5 and apply them

* Tue Sep 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Tue Aug 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Thu Aug 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.15.90-3mdv2007.0
- rebuild w/o selinux on x86_64

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.90-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Thu Jul 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-1mdv2007.0
- Release 2.15.2

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.1-1mdv2007.0
- Release 2.15.1
- Disable patches 3, 4, 5 for now

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1
- Regenerate patch0

* Wed Mar 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- Rebuild to remove howl dep

* Tue Feb 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdk
- New release 2.12.1
- use mkrel

* Thu Nov 17 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-2mdk
- rebuild for new openssl

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0
- Remove patches 1, 2 (merged upstream)
- Regenerate patch5

* Tue Sep 27 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-10mdk 
- Update patch5, read UTF-8 encoded url in .desktop file correctly

* Tue Sep 20 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-9mdk 
- Patch5: fix .desktop dir handling

* Thu Sep 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-8mdk 
- Patch4: fix desktop icon loading

* Sat Sep 03 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.1-7mdk
- rebuild to remove glitz dep

* Sat Aug 27 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-6mdk 
- Patch3 (CVS): check if .desktop points to existing directory

* Thu Aug 25 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-5mdk 
- Patch2 (CVS): various bugfixes from HEAD

* Tue Aug 02 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-4mdk 
- Patch1 (CVS): add support for .desktop file parsing

* Fri Jul 29 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-3mdk 
- Patch0: don't use gconf global settings for toolbar style, 
  uses xsettings instead.

* Sat Jul 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.10.1-2mdk
- fix provides on x86_64

* Thu Jul 07 2005 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdk
- drop patch
- New release 2.10.1

* Wed May 04 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-2mdk 
- Update patch0, better fix

* Wed Apr 20 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-1mdk 
- Release 2.10.0

* Wed Mar 02 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-2mdk 
- Patch0 : fix wrong gettext encoding for file selector backend for mozilla

* Mon Feb 21 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-1mdk 
- Release 2.8.1
- Remove patches 0 & 1 (merged upstream)

* Tue Jan 04 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-3mdk 
- Rebuild with latest howl

* Fri Dec 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-2mdk 
- Patch1 (CVS): improve filechooser vfs backend speed on big directories

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- New release 2.8.0
- Remove patch0 (merged upstream)
- Patch0 (Fedora): improve gnomevfs file chooser backend for ftp:

* Fri Sep 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.1.1-2mdk
- Patch0 (CVS): various bug and memleak fixes from CVS
- Enable libtoolize

* Mon May 03 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1.1-1mdk
- drop the patch
- New release 2.6.1.1

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- patch to make it build with gtk+ 2.4.0
- New release 2.6.1

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)

