%define api_version	2
%define lib_major	0
%define pkgname     libgnomeui
%define req_libbonoboui_version	2.13.0
%define req_libgnome_version	2.13.0
%define req_libgnomecanvas_version	2.0.0

%define libname		%mklibname gnomeui %{api_version} %{lib_major}
%define libnamedev	%mklibname -d gnomeui %{api_version}

Summary: Main GNOME libraries
Name: %{pkgname}%{api_version}
Version: 2.24.5
Release: %mkrel 2
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
# (fc) 2.22.1-2mdv link with math library
Patch0: libgnomeui-2.22.1-floor.patch
License: LGPLv2+
Url: http://www.gnome.org/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libbonoboui2-devel >= %{req_libbonoboui_version}
BuildRequires: libgnome2-devel >= %{req_libgnome_version}
BuildRequires: libgnomecanvas2-devel >= %{req_libgnomecanvas_version}
BuildRequires: libglade2.0-devel
BuildRequires: glib2-devel >= 2.15.5
BuildRequires: pango-devel >= 1.1.2
BuildRequires: gtk-doc >= 0.9
BuildRequires: libjpeg-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: gtk+2-devel >= 2.9.0
BuildRequires: libsm-devel
BuildRequires: intltool
BuildRequires: gnome-common
Requires: libbonoboui2 >= %{req_libbonoboui_version}
Requires: gnome-icon-theme

%description
Data files for the GNOME UI library such as translations.

%package -n %{libname}
Summary:	GNOME libraries
Group:		%{group}

Requires:	%{name} >= %{version}

%description -n %{libname}
GNOME library contains extra widgets to let your 
GNOME applications really shine

%package -n %{libnamedev}
Summary:	Static libraries, include files for GNOME
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gnomeui2-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Requires: libbonoboui2-devel >= %{req_libbonoboui_version}
Requires: libgnomecanvas2-devel >= %{req_libgnomecanvas_version}
Requires: libjpeg-devel
Obsoletes: %mklibname -d gnomeui %{api_version} 0

%description -n %{libnamedev}
Static library, headers files and documentation needed in order 
to develop applications using the GNOME library.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .floor

#needed by patch0
autoreconf -fi

%build
%configure2_5x --enable-gtk-doc

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{pkgname}-2.0

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a} \
 $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/filesystems/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
  
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -f %{pkgname}-2.0.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README 
%{_libdir}/libglade/2.0/*.so
%{_datadir}/pixmaps/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgnomeui-2.so.0*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a


