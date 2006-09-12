Summary:	C++ class library for daemons, clients and servers
Name:		rudiments
Version:	0.29
Release:	0.4
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/rudiments/%{name}-%{version}.tar.gz
# Source0-md5:	5f823e39cb89b6bcd309e3628ba48d3e
URL:		http://rudiments.sourceforge.net/
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rudiments is an Open Source C++ class library providing base classes
for things such as daemons, clients and servers, and wrapper classes
for the standard C functions for things like such as regular
expressions, semaphores and signal handling.

%package devel
Summary:	Libraries and header files for developing rudiments
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and header files for developing rudiments.

%package static
Summary:	static librarires for developing rudiments
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
static libraries files for developing rudiments.

%package doc
Summary:	Documentation for rudiments
Group:		Development/Libraries

%description doc
Documentation for rudiments.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librudiments-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rudiments
%{_libdir}/*.so
%attr(755,root,root) %{_bindir}/rudiments-config
%{_pkgconfigdir}/rudiments.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}
