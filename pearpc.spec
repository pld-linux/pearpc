Summary:	PowerPC emulator
Summary(pl):	Emulator PowerPC
Name:		pearpc
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/pearpc/%{name}-%{version}.tar.bz2
# Source0-md5:	d92ce39f1f8f80fad9ebe5f5f04e7bb4
URL:		http://pearpc.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
%ifarch %{ix86}
BuildRequires:	nasm
%endif
#BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Experimental emulator of PowerPC hardware, capable of running at least
MacOS X, Linux PPC and Darwin.

%description -l pl
Eksperymentalny emulator komputera PowerPC, umo¿liwiaj±cy uruchomienie
miêdzy innymi MacOS X, Linuksa PPC i Darwina.

%prep
%setup -q

%build
#QTDIR="%{_prefix}"
#CFLAGS="%{rpmcflags} -I%{_includedir}/qt"
#export QTDIR CFLAGS
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-ui=sdl \
%ifarch %ix86
	--enable-cpu=jitc_x86
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install video.x $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO ppccfg.example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}
