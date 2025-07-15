Summary:	GNU Serveez - server framework
Summary(pl.UTF-8):	GNU Serveez - szkielet serwerowy
Name:		serveez
Version:	0.3.1
Release:	1
License:	GPL v3+
Group:		Applications/Networking
Source0:	https://ftp.gnu.org/gnu/serveez/%{name}-%{version}.tar.lz
# Source0-md5:	02697fe81ff23365d956525ee0b6fd22
Patch0:		%{name}-info.patch
Patch1:		%{name}-format.patch
URL:		http://www.gnu.org/software/serveez/
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	guile-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	lzip
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Serveez is a server framework. It provides routines and help for
implementing IP-based servers (currently TCP, UDP and ICMP). It
supports named pipes for all connection-oriented protocols.

%description -l pl.UTF-8
GNU Serveez to szkielet serwerowy. Udostępnia funkcje i wsparcie przy
implementowaniu serwerów opartych na IP (obecnie TCP, UDP i ICMP).
Obsługuje nazwane potoki dla wszystkich protokołów opartych na
połączeniu.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/serveez
%{_datadir}/serveez
%{_infodir}/serveez.info*
%{_mandir}/man1/serveez.1*
