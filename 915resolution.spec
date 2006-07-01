Summary:	Change the resolution of an available vbios mode
Summary(pl):	Zmiana rozdzielczo�ci dost�pnych tryb�w vbios
Name:		915resolution
Version:	0.5.2
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://www.geocities.com/stomljen/%{name}-%{version}.tar.gz
# Source0-md5:	a3441e5662c5ff1e00dc97de4487e8f8
Source1:	%{name}.sysconfig
Source2:	%{name}.init
URL:		http://perso.wanadoo.fr/apoirier/
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
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

%description -l pl
915resolution to narz�dzie do modyfikowania BIOS-u graficznego uk�ad�w
graficznych Intela z serii 800 i 900. Obejmuje to uk�ady 845G, 855G i
865G, a tak�e 915G, 915GM i 945G. Zmiany te s� potrzebne, aby
umo�liwi� wy�wietlanie pewnych rozdzielczo�ci obrazu dla serwera
graficznego Xorg lub XFree86.

Modyfikacje wykonywane przez 915resolution w BIOS-ie nie s� trwa�e.
Nie ma niebezpiecze�stwa trwa�ej zmiany BIOS-u. Oznacza to tak�e, �e
915resolution musi by� uruchamiane przy ka�dym starcie komputera, aby
zmiany da�y efekt.

915resolution wywodzi si� z narz�dzia 855resolution. Jednak kod r�ni
si� znacz�co - kod 915resolution jest znacznie prostszy. 915resolution
pozwala dodatkowo na zmian� liczby bit�w na piksel.

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
