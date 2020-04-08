Summary:	A versatile deduplicating backup tool
Summary(pl.UTF-8):	Uniwersalne narzędzie do deduplikacji kopii zapasowych
Name:		zbackup
Version:	1.4.4
Release:	8
License:	GPL v2+ with OpenSSL Exception
Group:		Applications/Archiving
#Source0Download: https://github.com/zbackup/zbackup/releases
#TODO: Source0:	https://github.com/zbackup/zbackup/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/zbackup/zbackup/archive/%{version}.tar.gz
# Source0-md5:	0753ca5d61533f951d6ebb6f087efa0b
URL:		http://zbackup.org/
BuildRequires:	cmake >= 2.8.2
BuildRequires:	lzo-devel
BuildRequires:	openssl-devel
BuildRequires:	protobuf-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz-devel
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
zbackup jest narzędziem służącym do archiwizacji danych, opartym na
ideach rsynca i wykonujące deduplikację. Po przekazaniu mu dużego
pliku .tar, zapisuje powtórzone fragmenty tylko raz, następnie
kompresuje i opcjonalnie szyfruje wynik. Po przekazaniu kolejnego
pliku .tar używa ponownie danych znalezionych w dowolnej poprzedniej
kopii zapasowej. W ten sposób zapisywane są tylko nowe zmiany, a -
dopóki pliki nie różnią się bardzo - nie wymaga to dużo miejsca.

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
%doc CONTRIBUTORS LICENSE README.md
%attr(755,root,root) %{_bindir}/zbackup
