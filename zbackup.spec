Summary:	A versatile deduplicating backup tool
Summary(pl.UTF-8):	Uniwersalne narzędzie do deduplikacji kopii zapasowych
Name:		zbackup
Version:	1.4.4
Release:	5
License:	GPL v2+
Group:		Applications/Archiving
Source0:	https://github.com/zbackup/zbackup/archive/%{version}.tar.gz
# Source0-md5:	0753ca5d61533f951d6ebb6f087efa0b
URL:		http://zbackup.org/
BuildRequires:	cmake >= 2.8.2
BuildRequires:	lzma-devel
BuildRequires:	openssl-devel
BuildRequires:	protobuf-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zbackup is a globally-deduplicating backup tool, based on the ideas
found in rsync. Feed a large .tar into it, and it will store duplicate
regions of it only once, then compress and optionally encrypt the
result. Feed another .tar file, and it will also re-use any data found
in any previous backups. This way only new changes are stored, and as
long as the files are not very different, the amount of storage
required is very low.

%description -l pl.UTF-8
zbackup jest narzędziem służącym do archiwizacji danych, bazującym na
rsync i wykorzystujące deduplikację

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
