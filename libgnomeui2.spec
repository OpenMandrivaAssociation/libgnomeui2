%define api_version	2
%define lib_major	0
%define pkgname     libgnomeui

%define libname		%mklibname gnomeui %{api_version} %{lib_major}
%define develname	%mklibname -d gnomeui %{api_version}

Summary: Main GNOME libraries
Name: %{pkgname}%{api_version}
Version: 2.24.5
Release: 4
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
# (fc) 2.22.1-2mdv link with math library
Patch0: libgnomeui-2.22.1-floor.patch

BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: gtk-doc >= 0.9
BuildRequires: pkgconfig(gconf-2.0) >= 1.1.11
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires: pkgconfig(gio-2.0) >= 2.16.0
BuildRequires: pkgconfig(glib-2.0) >= 2.16.0
BuildRequires: pkgconfig(gnome-keyring-1) >= 0.4
BuildRequires: pkgconfig(gnome-vfs-2.0) >= 2.7.3
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libbonoboui-2.0) >= 2.13.1
BuildRequires: pkgconfig(libglade-2.0) >= 2.0.0
BuildRequires: pkgconfig(libgnome-2.0) >= 2.13.7
BuildRequires: pkgconfig(libgnomecanvas-2.0) >= 2.0.0
BuildRequires: pkgconfig(libxml-2.0) >= 2.4.20
BuildRequires: pkgconfig(pango) >= 1.1.2

Requires: gnome-icon-theme

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
Obsoletes: %mklibname -d gnomeui %{api_version} 0

%description -n %{develname}
Development library, headers files and documentation needed in order 
to develop applications using the GNOME library.

%prep
%setup -qn %{pkgname}-%{version}
%apply_patches

#needed by patch0
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{pkgname}-2.0

#remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

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

