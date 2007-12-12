%define name	videodog
%define version	0.31
%define release 1mdk

Name: 	 	%{name}
Summary: 	Video4Linux frame grabber
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://planeta.terra.com.br/informatica/gleicon/video4linux/videodog.html
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	jpeg-devel

%description
VideoDog is a command line tool to grab frames from a Video4linux-compliant
device. It can export a file in raw, PNM, or JPG formats. It can also do loop
capture using multiple buffers, or just be used to set/retrieve device data or
scripts. It presents a programming interface for implementing image
transformations and effects. There are some examples in the source code. No
external libraries are required.

%prep
%setup -q
mv %name.man %name.1
bzip2 %name.1

%build
%make CC="gcc $RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
%makeinstall
rm -fr %buildroot/usr/doc
cp vd.conf $RPM_BUILD_ROOT/%_sysconfdir
cp %name.1.bz2 $RPM_BUILD_ROOT/%_mandir/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ALPHABLEND CONFIG_FILE EFFECTS MOTION README CHANGELOG EFFECTS LICENSE TODO USAGE *.pdf
%{_bindir}/%name
%{_mandir}/man1/%name.1.bz2
%config(noreplace) %_sysconfdir/vd.conf

