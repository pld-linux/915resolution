#
Summary:	915resolution - changes the resolution of an available vbios mode.
Summary(pl):	915resolution
Name:		915resolution
Version:	0.5.2
Release:	0.1
License:	PUBLIC DOMAIN
Group:		Applications
Source0:	http://www.geocities.com/stomljen/%{name}-%{version}.tar.gz
# Source0-md5:	a3441e5662c5ff1e00dc97de4487e8f8
Patch0:		%{name}-DESTDIR.patch
URL:	http://www.geocities.com/stomljen/	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

This software changes the resolution of an available vbios mode.

It patches only the RAM version of the video bios so the new resolution
is loose each time you reboot. 
If you want to set the resolution each time you reboot and before to
launch X, use your rc.local, ... file of your Linux version.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.log chipset_info.txt README.txt LICENSE.txt
%attr(755,root,root) %{_sbindir}/*
