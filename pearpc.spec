Summary:	PowerPC emulator
Summary(pl):	Emulator PowerPC
Name:		pearpc
Version:	0.2.0
Release:	1
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	35820dba65afd73728451c94b4903a4a
License:	GPL
Group:		Applications/Emulators
Url:		http://pearpc.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	qt-devel >= 3.0
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
QTDIR="%{_prefix}"
CFLAGS="%{rpmcflags} -I%{_includedir}/qt"
export QTDIR CFLAGS
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gui=qt \
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
