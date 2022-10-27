#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vte
Version  : 0.70.1
Release  : 74
URL      : https://download.gnome.org/sources/vte/0.70/vte-0.70.1.tar.xz
Source0  : https://download.gnome.org/sources/vte/0.70/vte-0.70.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-4.0 GPL-3.0 LGPL-3.0 MIT
Requires: vte-bin = %{version}-%{release}
Requires: vte-data = %{version}-%{release}
Requires: vte-filemap = %{version}-%{release}
Requires: vte-lib = %{version}-%{release}
Requires: vte-libexec = %{version}-%{release}
Requires: vte-license = %{version}-%{release}
Requires: vte-locales = %{version}-%{release}
Requires: vte-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk3-dev
BuildRequires : intltool-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(libpcre2-8)
BuildRequires : vala-dev
Patch1: defaults.patch

%description
Virtual TErminal
================
VTE provides a virtual terminal widget for GTK applications.

%package bin
Summary: bin components for the vte package.
Group: Binaries
Requires: vte-data = %{version}-%{release}
Requires: vte-libexec = %{version}-%{release}
Requires: vte-license = %{version}-%{release}
Requires: vte-services = %{version}-%{release}
Requires: vte-filemap = %{version}-%{release}

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
Requires: vte-lib = %{version}-%{release}
Requires: vte-bin = %{version}-%{release}
Requires: vte-data = %{version}-%{release}
Provides: vte-devel = %{version}-%{release}
Requires: vte = %{version}-%{release}

%description dev
dev components for the vte package.


%package extras
Summary: extras components for the vte package.
Group: Default

%description extras
extras components for the vte package.


%package filemap
Summary: filemap components for the vte package.
Group: Default

%description filemap
filemap components for the vte package.


%package lib
Summary: lib components for the vte package.
Group: Libraries
Requires: vte-data = %{version}-%{release}
Requires: vte-libexec = %{version}-%{release}
Requires: vte-license = %{version}-%{release}
Requires: vte-filemap = %{version}-%{release}

%description lib
lib components for the vte package.


%package libexec
Summary: libexec components for the vte package.
Group: Default
Requires: vte-license = %{version}-%{release}
Requires: vte-filemap = %{version}-%{release}

%description libexec
libexec components for the vte package.


%package license
Summary: license components for the vte package.
Group: Default

%description license
license components for the vte package.


%package locales
Summary: locales components for the vte package.
Group: Default

%description locales
locales components for the vte package.


%package services
Summary: services components for the vte package.
Group: Systemd services

%description services
services components for the vte package.


%prep
%setup -q -n vte-0.70.1
cd %{_builddir}/vte-0.70.1
%patch1 -p1
pushd ..
cp -a vte-0.70.1 buildavx2
popd

%build
## build_prepend content
export CFLAGS="$CFLAGS -fexceptions"
export CXXFLAGS="$CFLAGS -fexceptions"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666845655
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk4=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk4=true  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/vte
cp %{_builddir}/vte-%{version}/COPYING.CC-BY-4-0 %{buildroot}/usr/share/package-licenses/vte/c0e2f3021a02d71ef52b88aac2ed98c996d7517d || :
cp %{_builddir}/vte-%{version}/COPYING.GPL3 %{buildroot}/usr/share/package-licenses/vte/a742ddd48b78f2a7a13ac678ce5ecacf93c771ee || :
cp %{_builddir}/vte-%{version}/COPYING.LGPL3 %{buildroot}/usr/share/package-licenses/vte/e203d4ef09d404fa5c03cf6590e44231665be689 || :
cp %{_builddir}/vte-%{version}/COPYING.XTERM %{buildroot}/usr/share/package-licenses/vte/704ec162c7e726301bf2b873fa99052b40250a99 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang vte-2.91
## install_append content
src=%{buildroot}/etc/profile.d/vte.sh
dest=%{buildroot}/usr/share/defaults/etc/profile.d
mkdir -p $dest
cp -a $src $dest/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vte-2.91
/usr/bin/vte-2.91-gtk4
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Vte-2.91.typelib
/usr/lib64/girepository-1.0/Vte-3.91.typelib
/usr/share/gir-1.0/*.gir
/usr/share/glade/catalogs/vte-2.91.xml
/usr/share/glade/pixmaps/hicolor/16x16/actions/widget-vte-terminal.png
/usr/share/glade/pixmaps/hicolor/22x22/actions/widget-vte-terminal.png
/usr/share/vala/vapi/vte-2.91-gtk4.deps
/usr/share/vala/vapi/vte-2.91-gtk4.vapi
/usr/share/vala/vapi/vte-2.91.deps
/usr/share/vala/vapi/vte-2.91.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/vte-2.91-gtk4/vte/vte.h
/usr/include/vte-2.91-gtk4/vte/vtedeprecated.h
/usr/include/vte-2.91-gtk4/vte/vteenums.h
/usr/include/vte-2.91-gtk4/vte/vteglobals.h
/usr/include/vte-2.91-gtk4/vte/vtemacros.h
/usr/include/vte-2.91-gtk4/vte/vtepty.h
/usr/include/vte-2.91-gtk4/vte/vteregex.h
/usr/include/vte-2.91-gtk4/vte/vteterminal.h
/usr/include/vte-2.91-gtk4/vte/vtetypebuiltins-gtk4.h
/usr/include/vte-2.91-gtk4/vte/vtetypebuiltins.h
/usr/include/vte-2.91-gtk4/vte/vteversion.h
/usr/include/vte-2.91/vte/vte.h
/usr/include/vte-2.91/vte/vtedeprecated.h
/usr/include/vte-2.91/vte/vteenums.h
/usr/include/vte-2.91/vte/vteglobals.h
/usr/include/vte-2.91/vte/vtemacros.h
/usr/include/vte-2.91/vte/vtepty.h
/usr/include/vte-2.91/vte/vteregex.h
/usr/include/vte-2.91/vte/vteterminal.h
/usr/include/vte-2.91/vte/vtetypebuiltins-gtk3.h
/usr/include/vte-2.91/vte/vtetypebuiltins.h
/usr/include/vte-2.91/vte/vteversion.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libvte-2.91-gtk4.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libvte-2.91.so
/usr/lib64/libvte-2.91-gtk4.so
/usr/lib64/libvte-2.91.so
/usr/lib64/pkgconfig/vte-2.91-gtk4.pc
/usr/lib64/pkgconfig/vte-2.91.pc

%files extras
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/vte.sh

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-vte

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libvte-2.91-gtk4.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libvte-2.91.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libvte-2.91.so.0.7000.1
/usr/lib64/libvte-2.91-gtk4.so.0
/usr/lib64/libvte-2.91.so.0
/usr/lib64/libvte-2.91.so.0.7000.1

%files libexec
%defattr(-,root,root,-)
/usr/libexec/vte-urlencode-cwd
/usr/share/clear/optimized-elf/exec*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vte/704ec162c7e726301bf2b873fa99052b40250a99
/usr/share/package-licenses/vte/a742ddd48b78f2a7a13ac678ce5ecacf93c771ee
/usr/share/package-licenses/vte/c0e2f3021a02d71ef52b88aac2ed98c996d7517d
/usr/share/package-licenses/vte/e203d4ef09d404fa5c03cf6590e44231665be689

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/vte-spawn-.scope.d/defaults.conf

%files locales -f vte-2.91.lang
%defattr(-,root,root,-)

