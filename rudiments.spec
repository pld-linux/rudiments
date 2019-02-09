Summary:	C++ class library for daemons, clients and servers
Summary(pl.UTF-8):	Biblioteka klas C++ dla demonów, klientów i serwerów
Name:		rudiments
Version:	1.1.0
Release:	5
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/rudiments/%{name}-%{version}.tar.gz
# Source0-md5:	0666bb3c3335551d10cdbe0dd6b61ce7
URL:		http://rudiments.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
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

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/librudiments.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librudiments.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rudiments-config
%attr(755,root,root) %{_libdir}/librudiments.so
%{_libdir}/librudiments.la
%{_includedir}/rudiments
%{_pkgconfigdir}/rudiments.pc
%{_mandir}/man1/rudiments-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/librudiments.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}
