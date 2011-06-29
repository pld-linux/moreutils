# TODO:
# - Subpackage each tool?
Summary:	A collection of unix tools
Name:		moreutils
Version:	0.45
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/m/moreutils/%{name}_%{version}.tar.gz
# Source0-md5:	b30306cd7312219551b890fbcbf984c4
Patch0:		%{name}-make.patch
URL:		http://kitenet.net/~joey/code/moreutils/
BuildRequires:	docbook-dtd44-sgml
BuildRequires:	docbook2X
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of unix tools that nobody thought to write long ago, when
unix was young. Currently it consists of these tools:

 - chronic: runs a command quietly unless it fails
 - ccombine: combine the lines in two files using boolean operations
 - ifdata: get network interface info without parsing ifconfig output
 - isutf8: check if a file or standard input is utf-8
 - ifne: run a command if the standard input is not empty
 - lckdo: execute a program with a lock held (deprecated)
 - mispipe: pipe two commands, returning the exit status of the first
 - parallel: run multiple jobs at once
 - pee: tee standard input to pipes
 - sponge: soak up standard input and write to a file
 - ts: timestamp standard input
 - vidir: edit a directory in your text editor
 - vipe: insert a text editor into a pipe
 - zrun: automatically uncompress arguments to command

%prep
%setup -q -n %{name}
%patch0 -p1
%{__sed} -i -e '/"file:\/\/\/.*docbookx\.dtd"/d' *docbook
%{__sed} -i -e '/xml version="1.0" encoding="utf-8"/d' *docbook

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING
%attr(755,root,root) %{_bindir}/chronic
%attr(755,root,root) %{_bindir}/combine
%attr(755,root,root) %{_bindir}/ifdata
%attr(755,root,root) %{_bindir}/ifne
%attr(755,root,root) %{_bindir}/isutf8
%attr(755,root,root) %{_bindir}/lckdo
%attr(755,root,root) %{_bindir}/mispipe
%attr(755,root,root) %{_bindir}/parallel
%attr(755,root,root) %{_bindir}/pee
%attr(755,root,root) %{_bindir}/sponge
%attr(755,root,root) %{_bindir}/ts
%attr(755,root,root) %{_bindir}/vidir
%attr(755,root,root) %{_bindir}/vipe
%attr(755,root,root) %{_bindir}/zrun
%{_mandir}/man1/*.1*
