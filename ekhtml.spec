Summary:	ekhtml is a speedy html parser
Name:		ekhtml
Version:	0.3.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://ekhtml.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ekhtml is a speedy, yet forgiving, SAX-stylee HTML parser.

%package devel
Summary:	Header files for ekhtml
Summary(pl):	Pliki nag³ówkowe do ekhtml
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for ekhtml.

%description devel -l pl
Pliki nag³ówkowe do ekhtml.

%package static
Summary:	Static ekhtml libraries
Summary(pl):	Biblioteka statyczna ekhtml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static ekhtml libraries.

%description static -l pl
Biblioteka statyczna ekhtml.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
