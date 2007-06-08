Summary:	C++ class library for daemons, clients and servers
Summary(pl.UTF-8):	Biblioteka klas C++ dla demonów, klientów i serwerów
Name:		rudiments
Version:	0.30
Release:	2
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/rudiments/%{name}-%{version}.tar.gz
# Source0-md5:	5fed91a1e01eb8bb821f306d74226086
URL:		http://rudiments.sourceforge.net/
BuildRequires:	automake
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
%attr(755,root,root) %{_libdir}/librudiments-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rudiments-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/rudiments
%{_pkgconfigdir}/rudiments.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}
