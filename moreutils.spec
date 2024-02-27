Summary:	A collection of unix tools
Summary(pl.UTF-8):	Zestaw narzędzi uniksowych
Name:		moreutils
Version:	0.69
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/m/moreutils/%{name}_%{version}.orig.tar.xz
# Source0-md5:	2a2b101efa55149c44fd761a3070395b
URL:		http://joeyh.name/code/moreutils/
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	perl-tools-pod
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of unix tools that nobody thought to write long ago, when
unix was young. Currently it consists of these tools:

 - chronic: runs a command quietly unless it fails
 - ccombine: combine the lines in two files using boolean operations
 - errno: look up errno names and descriptions
 - ifdata: get network interface info without parsing ifconfig output
 - isutf8: check if a file or standard input is utf-8
 - ifne: run a command if the standard input is not empty
 - lckdo: execute a program with a lock held (deprecated)
 - mispipe: pipe two commands, returning the exit status of the first
 - pee: tee standard input to pipes
 - sponge: soak up standard input and write to a file
 - ts: timestamp standard input
 - vidir: edit a directory in your text editor
 - vipe: insert a text editor into a pipe
 - zrun: automatically uncompress arguments to command

%description -l pl.UTF-8
Zestaw narzędzi uniksowych, o których napisaniu nikt nie pomyślał
dawno temu, kiedy unix był młody. Obecnie zawiera następujące
narzędzia:

 - chronic: ciche uruchomienie polecenia, jeśli nie ma błędu
 - ccombine: łączenie linii z dwóch plików przy użyciu operacji
   logicznych
 - errno: wyszukiwanie nazw i opisów errno
 - ifdata: pobieranie informacji o interfejsie bez analizy wyjścia
   ifconfiga
 - isutf8: sprawdzenie, czy lub standardowe wejście jest w UTF-8
 - ifne: uruchomienie polecenia, jeśli standardowe wejście nie jest
   puste
 - lckdo: uruchomienie programu podczas trzymania blokady
   (przestarzały)
 - mispipe: potok dwóch poleceń, zwracający status zakończenia
   pierwszego z nich
 - pee: tee standardowego wejścia do potoków
 - sponge: przesączenie standardowego wejścia i zapis do pliku
 - ts: oznaczenie standardowego wejścia znacznikami czasu
 - vidir: edycja katalogu w edytorze tekstu
 - vipe: wstawienie edytora tekstu w potok
 - zrun: automatyczne dekompresja argumentów polecenia

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -Wall" \
	DOCBOOKXSL=%{_datadir}/sgml/docbook/xsl-nons-stylesheets

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_BIN=install

# use parallel package instead
%{__rm} $RPM_BUILD_ROOT%{_bindir}/parallel
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/parallel.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README debian/changelog
%attr(755,root,root) %{_bindir}/chronic
%attr(755,root,root) %{_bindir}/combine
%attr(755,root,root) %{_bindir}/errno
%attr(755,root,root) %{_bindir}/ifdata
%attr(755,root,root) %{_bindir}/ifne
%attr(755,root,root) %{_bindir}/isutf8
%attr(755,root,root) %{_bindir}/lckdo
%attr(755,root,root) %{_bindir}/mispipe
%attr(755,root,root) %{_bindir}/pee
%attr(755,root,root) %{_bindir}/sponge
%attr(755,root,root) %{_bindir}/ts
%attr(755,root,root) %{_bindir}/vidir
%attr(755,root,root) %{_bindir}/vipe
%attr(755,root,root) %{_bindir}/zrun
%{_mandir}/man1/chronic.1*
%{_mandir}/man1/combine.1*
%{_mandir}/man1/errno.1*
%{_mandir}/man1/ifdata.1*
%{_mandir}/man1/ifne.1*
%{_mandir}/man1/isutf8.1*
%{_mandir}/man1/lckdo.1*
%{_mandir}/man1/mispipe.1*
%{_mandir}/man1/pee.1*
%{_mandir}/man1/sponge.1*
%{_mandir}/man1/ts.1*
%{_mandir}/man1/vidir.1*
%{_mandir}/man1/vipe.1*
%{_mandir}/man1/zrun.1*
