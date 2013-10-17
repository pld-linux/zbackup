Summary:	A versatile deduplicating backup tool
Summary(pl.UTF-8):	Uniwersalne narzÄdzie do deduplikacji kopii zapasowych
Name:		zbackup
Version:	1.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
# Source0-md5:	e816af0e1381a35236488dbe86003d14
URL:		http://zbackup.org/
BuildRequires:	cmake >= 2.8.2
BuildRequires:	lzma-devel
BuildRequires:	openssl-devel
BuildRequires:	protobuf-devel
BuildRequires:	zlib-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zbackup is a globally-deduplicating backup tool, based on the ideas found in rsync.
Feed a large .tar into it, and it will store duplicate regions of it only once,
then compress and optionally encrypt the result. Feed another .tar file,
and it will also re-use any data found in any previous backups.
This way only new changes are stored, and as long as the files are
not very different, the amount of storage required is very low.
%description -l pl.UTF-8
zbackup jest narzÄdziem sÅuÅ¼Äcym do archiwizacji danyc,
bazujÄcym na rsync i wykorzystujÄce deduplikacjÄ

%prep
%setup -q

%build
%cmake . 
#\
#	-CMAKE_INSTALL_PREFIX=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}

