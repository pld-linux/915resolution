# TODO - http://archive.ubuntu.com/ubuntu/pool/universe/9/915resolution/915resolution_0.5-1ubuntu6.diff.gz
#
Summary:	Change the resolution of an available vbios mode
Summary(pl.UTF-8):   Zmiana rozdzielczości dostępnych trybów vbios
Name:		915resolution
Version:	0.5.2
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://www.geocities.com/stomljen/%{name}-%{version}.tar.gz
# Source0-md5:	a3441e5662c5ff1e00dc97de4487e8f8
Source1:	%{name}.sysconfig
Source2:	%{name}.init
URL:		http://www.geocities.com/stomljen/
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
915resolution is a tool to modify the video BIOS of the 800 and
900 series Intel graphics chipsets. This includes the 845G, 855G,
and 865G chipsets, as well as 915G, 915GM, and 945G chipsets. This
modification is neccessary to allow the display of certain graphics
resolutions for an Xorg or XFree86 graphics server.

915resolution's modifications of the BIOS are transient. There is
no risk of permanent modification of the BIOS. This also means that
915resolution must be run every time the computer boots inorder for
it's changes to take effect.

915resolution is derived from the tool 855resolution. However,
the code differs substantially. 915resolution's code base is much
simpler. 915resolution also allows the modification of bits per pixel.

%description -l pl.UTF-8
915resolution to narzędzie do modyfikowania BIOS-u graficznego układów
graficznych Intela z serii 800 i 900. Obejmuje to układy 845G, 855G i
865G, a także 915G, 915GM i 945G. Zmiany te są potrzebne, aby
umożliwić wyświetlanie pewnych rozdzielczości obrazu dla serwera
graficznego Xorg lub XFree86.

Modyfikacje wykonywane przez 915resolution w BIOS-ie nie są trwałe.
Nie ma niebezpieczeństwa trwałej zmiany BIOS-u. Oznacza to także, że
915resolution musi być uruchamiane przy każdym starcie komputera, aby
zmiany dały efekt.

915resolution wywodzi się z narzędzia 855resolution. Jednak kod różni
się znacząco - kod 915resolution jest znacznie prostszy. 915resolution
pozwala dodatkowo na zmianę liczby bitów na piksel.

%prep
%setup -q

%build
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,sysconfig}}

install 915resolution $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add 915resolution

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del 915resolution
fi

%files
%defattr(644,root,root,755)
%doc changes* chipset_info.txt README.txt
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) %{_sbindir}/*
