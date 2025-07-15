#
# Conditional build:
%bcond_with	apache	# Apache 2 support (too messy for now, adds flags to librudiments)

Summary:	C++ class library for daemons, clients and servers
Summary(pl.UTF-8):	Biblioteka klas C++ dla demonów, klientów i serwerów
Name:		rudiments
Version:	1.3.0
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/rudiments/%{name}-%{version}.tar.gz
# Source0-md5:	06e5e81901f8bd6d2a9f0b2b1a4f9993
Patch0:		%{name}-pc.patch
URL:		http://rudiments.sourceforge.net/
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.15.2
BuildRequires:	heimdal-devel
BuildRequires:	libedit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
%if %{with apache}
BuildRequires:	apache-devel >= 2
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
%endif
Requires:	curl-libs >= 7.15.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rudiments is an Open Source C++ class library providing base classes
for things such as daemons, clients and servers, and wrapper classes
for the standard C functions for things like such as regular
expressions, semaphores and signal handling.

%description -l pl.UTF-8
Rudiments to mająca otwarte źródła biblioteka klas C++ dostarczająca
klasy bazowe do tworzenia demonów, klientów i serwerów oraz klasy
obudowujące dla standardowych funkcji C obsługujących wyrażenia
regularne, semafory, sygnały itp.

%package devel
Summary:	Header files for rudiments library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rudiments
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.15.2
Requires:	heimdal-devel
Requires:	libedit-devel
Requires:	libstdc++-devel
Requires:	openssl-devel
Requires:	pcre-devel

%description devel
Header files for rudiments library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki rudiments.

%package static
Summary:	Static rudiments library
Summary(pl.UTF-8):	Statyczna biblioteka rudiments
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static rudiments library.

%description static -l pl.UTF-8
Statyczna biblioteka rudiments.

%package doc
Summary:	Documentation for rudiments
Summary(pl.UTF-8):	Dokumentacja dla biblioteki rudiments
Group:		Documentation

%description doc
Documentation for rudiments.

%description doc -l pl.UTF-8
Dokumentacja dla biblioteki rudiments.

%prep
%setup -q
%patch -P0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	%{!?with_apache:--disable-apache2}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{systemdtmpfilesdir}
cat >$RPM_BUILD_ROOT%{systemdtmpfilesdir}/rudiments.conf <<EOF
d /var/run/rudiments 1777 root root -
EOF

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librudiments.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/librudiments.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librudiments.so.7
%attr(1777,root,root) %dir /var/run/rudiments
%{systemdtmpfilesdir}/rudiments.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rudiments-config
%attr(755,root,root) %{_libdir}/librudiments.so
%{_includedir}/rudiments
%{_pkgconfigdir}/rudiments.pc
%{_mandir}/man1/rudiments-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/librudiments.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}
