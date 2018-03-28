#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vte
Version  : 0.52.0
Release  : 24
URL      : https://github.com/GNOME/vte/archive/0.52.0.tar.gz
Source0  : https://github.com/GNOME/vte/archive/0.52.0.tar.gz
Summary  : Vte terminal widget.
Group    : Development/Tools
License  : LGPL-2.1
Requires: vte-bin
Requires: vte-data
Requires: vte-lib
Requires: vte-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pcre-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libpcre2-8)
BuildRequires : pkgconfig(pango)
BuildRequires : sed
Patch1: defaults.patch

%description
* What is VTE?
VTE is a library (libvte) implementing a terminal emulator widget for GTK+,
and a minimal sample application (vte) using that.  Vte is mainly used in
gnome-terminal, but can also be used to embed a console/terminal in games,
editors, IDEs, etc.

%package bin
Summary: bin components for the vte package.
Group: Binaries
Requires: vte-data

%description bin
bin components for the vte package.


%package data
Summary: data components for the vte package.
Group: Data

%description data
data components for the vte package.


%package dev
Summary: dev components for the vte package.
Group: Development
Requires: vte-lib
Requires: vte-bin
Requires: vte-data
Provides: vte-devel

%description dev
dev components for the vte package.


%package lib
Summary: lib components for the vte package.
Group: Libraries
Requires: vte-data

%description lib
lib components for the vte package.


%package locales
Summary: locales components for the vte package.
Group: Default

%description locales
locales components for the vte package.


%prep
%setup -q -n vte-0.52.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522219455
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%autogen --disable-static --enable-vala=no
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1522219455
rm -rf %{buildroot}
%make_install
%find_lang vte-2.91

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vte-2.91

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Vte-2.91.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/vte-2.91/vte/vte.h
/usr/include/vte-2.91/vte/vtedeprecated.h
/usr/include/vte-2.91/vte/vteenums.h
/usr/include/vte-2.91/vte/vteglobals.h
/usr/include/vte-2.91/vte/vtemacros.h
/usr/include/vte-2.91/vte/vtepty.h
/usr/include/vte-2.91/vte/vteregex.h
/usr/include/vte-2.91/vte/vteterminal.h
/usr/include/vte-2.91/vte/vtetypebuiltins.h
/usr/include/vte-2.91/vte/vteversion.h
/usr/lib64/libvte-2.91.so
/usr/lib64/pkgconfig/vte-2.91.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvte-2.91.so.0
/usr/lib64/libvte-2.91.so.0.5200.0

%files locales -f vte-2.91.lang
%defattr(-,root,root,-)

