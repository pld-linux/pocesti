Summary:	Pocesti
Summary(pl):	Pocesti
Name:		pocesti
Version:	0.5
Release:	2
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://gnu.arachne.cz/%{name}-%{version}.tar.gz
URL:		http://gnu.arachne.cz/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pocesti is similar to ogonkify, but provides unicode support, which is
helpful for printing ISO-8859-2 characters from Mozilla.

%description -l pl
Pocesti jest programem podobnym do ogonkify, ale zawiera wsparcie dla
unicode, dzi�ki czemu mo�liwy jest poprawny wydruk polskich znak�w
spod Mozilli.

%prep
%setup -q

%build
gcc -o pocesti pocesti.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

cp -f pocesti $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README FIXEDBUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%doc *.gz
%{_bindir}/*
