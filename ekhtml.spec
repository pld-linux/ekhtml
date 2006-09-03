Summary:	ekhtml - a speedy HTML parser
Summary(pl):	ekhtml - szybki analizator HTML-a
Name:		ekhtml
Version:	0.3.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/ekhtml/%{name}-%{version}.tar.gz
# Source0-md5:	cc9d2e4adaccacfacefddbd75ccccfdf
URL:		http://ekhtml.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ekhtml is a speedy, yet forgiving, SAX-style HTML parser.

%description -l pl
ekhtml to szybki ale odpuszczaj±cy analizator HTML-a w stylu SAX.

%package devel
Summary:	Header files for ekhtml
Summary(pl):	Pliki nag³ówkowe do ekhtml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ekhtml.

%description devel -l pl
Pliki nag³ówkowe do ekhtml.

%package static
Summary:	Static ekhtml library
Summary(pl):	Biblioteka statyczna ekhtml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ekhtml library.

%description static -l pl
Biblioteka statyczna ekhtml.

%prep
%setup -q

%build
%configure
%{__make} -j1

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
%doc ChangeLog README AUTHORS NEWS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
