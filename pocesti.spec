Summary:	Pocesti - utility similar to ogonkify
Summary(pl.UTF-8):   Pocesti - narzędzie podobne do ogonkify
Name:		pocesti
Version:	0.6
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	http://gnu.arachne.cz/%{name}-%{version}.tar.gz
# Source0-md5:	6767f4df8f5178644eaf74e911120408
URL:		http://gnu.arachne.cz/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pocesti is similar to ogonkify, but provides unicode support, which is
helpful for printing ISO-8859-2 characters from Mozilla.

%description -l pl.UTF-8
Pocesti jest programem podobnym do ogonkify, ale zawiera wsparcie dla
unicode, dzięki czemu możliwy jest poprawny wydruk polskich znaków
spod Mozilli.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o pocesti pocesti.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pocesti $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FIXEDBUGS
%attr(755,root,root) %{_bindir}/*
