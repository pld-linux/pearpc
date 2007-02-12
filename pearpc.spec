# TODO:
#	- ifppc_up/down scripts
#
# Conditional build:
%bcond_without	x11	# at last one nead to be specified \
%bcond_without	sdl	# or you will get useless package
%bcond_with	qt	# not finished
%bcond_with	gtk	# not finished
#
Summary:	PowerPC emulator
Summary(pl.UTF-8):   Emulator PowerPC
Name:		pearpc
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/pearpc/%{name}-%{version}.tar.bz2
# Source0-md5:	cc317b19d61a49987f2265e885fa6301
Source1:	%{name}.start
Source2:	%{name}.desktop
Patch0:		%{name}-ptrsize.patch
URL:		http://pearpc.sourceforge.net/
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.0}
%{?with_x11:BuildRequires:	XFree86-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
%{?with_gtk:BuildRequires:	gtk+2-devel}
BuildRequires:	libstdc++-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
%{?with_qt:BuildRequires:	qt-devel >= 3.0}
BuildRequires:	sed >= 4.0
Requires:	%{name}-bin = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Experimental emulator of PowerPC hardware, capable of running at least
MacOS X, Linux PPC and Darwin.

%description -l pl.UTF-8
Eksperymentalny emulator komputera PowerPC, umożliwiający uruchomienie
między innymi MacOS X, Linuksa PPC i Darwina.

%package x11
Summary:	X11 PearPC version
Summary(pl.UTF-8):   Wersja X11 PearPC
Group:		Applications/Emulators
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-bin = %{version}-%{release}

%description x11
X11 PearPC version.

%description x11 -l pl.UTF-8
Wersja X11 PearPC.

%package sdl
Summary:	SDL PearPC version
Summary(pl.UTF-8):   Wersja SDL PearPC
Group:		Applications/Emulators
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-bin = %{version}-%{release}

%description sdl
SDL PearPC version.

%description sdl -l pl.UTF-8
Wersja SDL PearPC.

%package qt
Summary:	Qt PearPC version
Summary(pl.UTF-8):   Wersja Qt PearPC
Group:		Applications/Emulators
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-bin = %{version}-%{release}

%description qt
Qt PearPC version.

%description qt -l pl.UTF-8
Wersja Qt PearPC.

%package gtk
Summary:	GTK+ PearPC version
Summary(pl.UTF-8):   Wersja GTK+ PearPC
Group:		Applications/Emulators
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-bin = %{version}-%{release}

%description gtk
GTK+ PearPC version.

%description gtk -l pl.UTF-8
Wersja GTK+ PearPC.

%prep
%setup -q
%patch0 -p1
sed 's@video\.x@%{_datadir}/%{name}/video.x@' \
	-i ppccfg.example

%build
#QTDIR="%{_prefix}"
#CFLAGS="%{rpmcflags} -I%{_includedir}/qt"
#export QTDIR CFLAGS
%{__aclocal}
%{__autoconf}
%{__automake}
for UI in %{?with_x11:x11} %{?with_sdl:sdl} %{?with_qt:qt} %{?with_gtk:gtk}; do

%configure \
%ifarch %{ix86}
	--enable-cpu=jitc_x86 \
%endif
	--enable-ui=$UI \
	%{!?debug:--disable-debug}

%{__make}
mv src/ppc ppc.$UI

done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1,%{_desktopdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ppc
%{?with_x11:install ppc.x11 $RPM_BUILD_ROOT%{_bindir}}
%{?with_sdl:install ppc.sdl $RPM_BUILD_ROOT%{_bindir}}
%{?with_qt:install ppc.qt $RPM_BUILD_ROOT%{_bindir}}
%{?with_gtk:install ppc.gtk $RPM_BUILD_ROOT%{_bindir}}
install video.x $RPM_BUILD_ROOT%{_datadir}/%{name}
install doc/ppc.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO ppccfg.example
%attr(755,root,root) %{_bindir}/ppc
%{_mandir}/man?/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop

%if %{with x11}
%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppc.x11
%endif

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppc.sdl
%endif

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppc.qt
%endif

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppc.gtk
%endif
