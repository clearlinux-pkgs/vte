#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vte
Version  : 0.28.2
Release  : 8
URL      : http://ftp.gnome.org/pub/GNOME/sources/vte/0.28/vte-0.28.2.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/vte/0.28/vte-0.28.2.tar.xz
Summary  : Vte terminal widget.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: vte-bin
Requires: vte-lib
Requires: vte-doc
Requires: vte-locales
Requires: vte-data
BuildRequires : gettext
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : ncurses-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : sed
Patch1: cve-2012-2738.patch

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

%description dev
dev components for the vte package.


%package doc
Summary: doc components for the vte package.
Group: Documentation

%description doc
doc components for the vte package.


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
%setup -q -n vte-0.28.2
%patch1 -p1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang vte-0.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vte
/usr/libexec/gnome-pty-helper

%files data
%defattr(-,root,root,-)
/usr/share/vte/termcap-0.0/xterm

%files dev
%defattr(-,root,root,-)
/usr/include/vte-0.0/vte/pty.h
/usr/include/vte-0.0/vte/reaper.h
/usr/include/vte-0.0/vte/vte.h
/usr/include/vte-0.0/vte/vteaccess.h
/usr/include/vte-0.0/vte/vtedeprecated.h
/usr/include/vte-0.0/vte/vtepty.h
/usr/include/vte-0.0/vte/vtetypebuiltins.h
/usr/include/vte-0.0/vte/vteversion.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/vte-0.0/VteReaper.html
/usr/share/gtk-doc/html/vte-0.0/VteTerminal.html
/usr/share/gtk-doc/html/vte-0.0/VteTerminalAccessible.html
/usr/share/gtk-doc/html/vte-0.0/annotation-glossary.html
/usr/share/gtk-doc/html/vte-0.0/api-index-0-20.html
/usr/share/gtk-doc/html/vte-0.0/api-index-0-24.html
/usr/share/gtk-doc/html/vte-0.0/api-index-0-26.html
/usr/share/gtk-doc/html/vte-0.0/api-index-0-28.html
/usr/share/gtk-doc/html/vte-0.0/api-index-deprecated.html
/usr/share/gtk-doc/html/vte-0.0/api-index-full.html
/usr/share/gtk-doc/html/vte-0.0/ch01.html
/usr/share/gtk-doc/html/vte-0.0/ch02.html
/usr/share/gtk-doc/html/vte-0.0/ch03.html
/usr/share/gtk-doc/html/vte-0.0/deprecated-objects.html
/usr/share/gtk-doc/html/vte-0.0/home.png
/usr/share/gtk-doc/html/vte-0.0/index.html
/usr/share/gtk-doc/html/vte-0.0/index.sgml
/usr/share/gtk-doc/html/vte-0.0/internal-objects.html
/usr/share/gtk-doc/html/vte-0.0/left.png
/usr/share/gtk-doc/html/vte-0.0/licence.html
/usr/share/gtk-doc/html/vte-0.0/object-hierarchy.html
/usr/share/gtk-doc/html/vte-0.0/pt01.html
/usr/share/gtk-doc/html/vte-0.0/right.png
/usr/share/gtk-doc/html/vte-0.0/style.css
/usr/share/gtk-doc/html/vte-0.0/up.png
/usr/share/gtk-doc/html/vte-0.0/vte-0.0.devhelp
/usr/share/gtk-doc/html/vte-0.0/vte-0.0.devhelp2
/usr/share/gtk-doc/html/vte-0.0/vte-Version-Information.html
/usr/share/gtk-doc/html/vte-0.0/vte-Vte-PTY.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f vte-0.0.lang 
%defattr(-,root,root,-)
