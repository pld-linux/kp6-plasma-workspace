#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
%define		kdeplasmaver	6.3.0
%define		qtver		6.6.0
%define		kf6ver		6.2.0
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Name:		kp6-%{kpname}
Version:	6.3.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	43eedae7b78e7286a8ac7af5b91ed910
Source1:	kde.pam
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt6-devel >= 1.0
BuildRequires:	PackageKit-qt6-devel
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Positioning-devel >= %{qtver}
BuildRequires:	Qt6PrintSupport-devel >= %{qtver}
BuildRequires:	Qt6Qt5Compat-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6ShaderTools-devel >= %{qtver}
BuildRequires:	Qt6Sql-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6WaylandClient-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.22
BuildRequires:	fontconfig-devel
BuildRequires:	gpsd-devel
BuildRequires:	iso-codes
BuildRequires:	ka6-kio-extras-devel
BuildRequires:	ka6-libkexiv2-devel
BuildRequires:	kf6-baloo-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kf6ver}
BuildRequires:	kf6-karchive-devel >= %{kf6ver}
BuildRequires:	kf6-kauth-devel >= %{kf6ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf6ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kcrash-devel >= %{kf6ver}
BuildRequires:	kf6-kdbusaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kdeclarative-devel >= %{kf6ver}
BuildRequires:	kf6-kded-devel
BuildRequires:	kf6-kdoctools-devel >= %{kf6ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf6ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kholidays-devel >= %{kf6ver}
BuildRequires:	kf6-ki18n-devel >= %{kf6ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf6ver}
BuildRequires:	kf6-kidletime-devel >= %{kf6ver}
BuildRequires:	kf6-kio-devel >= %{kf6ver}
BuildRequires:	kf6-kirigami-devel >= %{kf6ver}
BuildRequires:	kf6-kitemmodels-devel >= %{kf6ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf6ver}
BuildRequires:	kf6-knotifications-devel >= %{kf6ver}
BuildRequires:	kf6-knotifyconfig-devel >= %{kf6ver}
BuildRequires:	kf6-kpackage-devel >= %{kf6ver}
BuildRequires:	kf6-kpeople-devel >= %{kf6ver}
BuildRequires:	kf6-kquickcharts-devel >= %{kf6ver}
BuildRequires:	kf6-krunner-devel >= %{kf6ver}
BuildRequires:	kf6-kstatusnotifieritem-devel >= %{kf6ver}
BuildRequires:	kf6-ksvg-devel >= %{kf6ver}
BuildRequires:	kf6-ktexteditor-devel >= %{kf6ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf6ver}
BuildRequires:	kf6-kunitconversion-devel >= %{kf6ver}
BuildRequires:	kf6-kwallet-devel >= %{kf6ver}
BuildRequires:	kf6-networkmanager-qt-devel >= %{kf6ver}
BuildRequires:	kf6-prison-devel >= %{kf6ver}
BuildRequires:	kp6-breeze-devel >= %{kdeplasmaver}
BuildRequires:	kp6-kpipewire-devel >= %{kdeplasmaver}
BuildRequires:	kp6-kscreenlocker-devel >= %{kdeplasmaver}
BuildRequires:	kp6-kwayland-devel >= %{kdeplasmaver}
BuildRequires:	kp6-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp6-layer-shell-qt-devel >= %{kdeplasmaver}
BuildRequires:	kp6-libkscreen-devel >= %{kdeplasmaver}
BuildRequires:	kp6-libksysguard-devel >= %{kdeplasmaver}
BuildRequires:	kp6-libplasma-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma-activities-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma-activities-stats-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma5support-devel >= %{kdeplasmaver}
BuildRequires:	kuserfeedback-devel
BuildRequires:	libdrm-devel
BuildRequires:	libicu-devel
BuildRequires:	libqalculate-devel > 2.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel >= 4.6.60
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	plasma-wayland-protocols-devel >= 1.6
BuildRequires:	polkit-qt6-1-devel
BuildRequires:	qcoro-qt6-devel
BuildRequires:	qt6-shadertools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.31
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kp6-plasma-workspace-data = %{version}-%{release}
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KDE Plasma Workspace.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
Obsoletes:	kp5-%{kpname}-data < %{version}
BuildArch:	noarch

%description data
Data for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kp5-%{kpname}-devel < %{version}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -p -D %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/kde

# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,tok}
sed -i -e 's|/usr/bin/env python3|%{_bindir}/python3|' $RPM_BUILD_ROOT%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.py

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
/etc/xdg/autostart/gmenudbusmenuproxy.desktop
/etc/xdg/autostart/org.kde.plasmashell.desktop
/etc/xdg/autostart/org.kde.plasma-fallback-session-restore.desktop
/etc/xdg/autostart/xembedsniproxy.desktop
/etc/xdg/menus/plasma-applications.menu
/etc/xdg/plasmanotifyrc
/etc/xdg/taskmanagerrulesrc
%attr(755,root,root) %{_bindir}/gmenudbusmenuproxy
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kcolorschemeeditor
%attr(755,root,root) %{_bindir}/kde-systemd-start-condition
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_bindir}/krunner
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplashqml
%attr(755,root,root) %{_bindir}/lookandfeeltool
%attr(755,root,root) %{_bindir}/plasma-apply-colorscheme
%attr(755,root,root) %{_bindir}/plasma-apply-cursortheme
%attr(755,root,root) %{_bindir}/plasma-apply-desktoptheme
%attr(755,root,root) %{_bindir}/plasma-apply-lookandfeel
%attr(755,root,root) %{_bindir}/plasma-apply-wallpaperimage
%attr(755,root,root) %{_bindir}/plasma-interactiveconsole
%attr(755,root,root) %{_bindir}/plasma-localegen-helper
%attr(755,root,root) %{_bindir}/plasma-shutdown
%attr(755,root,root) %{_bindir}/plasma_session
%attr(755,root,root) %{_bindir}/plasma_waitforname
%attr(755,root,root) %{_bindir}/plasmashell
%attr(755,root,root) %{_bindir}/plasmawindowed
%attr(755,root,root) %{_bindir}/startplasma-wayland
%attr(755,root,root) %{_bindir}/startplasma-x11
%attr(755,root,root) %{_bindir}/xembedsniproxy
%{systemduserunitdir}/plasma-baloorunner.service
%{systemduserunitdir}/plasma-core.target
%{systemduserunitdir}/plasma-gmenudbusmenuproxy.service
%{systemduserunitdir}/plasma-kcminit-phase1.service
%{systemduserunitdir}/plasma-kcminit.service
%{systemduserunitdir}/plasma-krunner.service
%{systemduserunitdir}/plasma-ksmserver.service
%{systemduserunitdir}/plasma-ksplash-ready.service
%{systemduserunitdir}/plasma-ksplash.service
%{systemduserunitdir}/plasma-plasmashell.service
%{systemduserunitdir}/plasma-restoresession.service
%{systemduserunitdir}/plasma-workspace-wayland.target
%{systemduserunitdir}/plasma-workspace-x11.target
%{systemduserunitdir}/plasma-workspace.target
%{systemduserunitdir}/plasma-xembedsniproxy.service
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%ghost %{_libdir}/libcolorcorrect.so.6
%attr(755,root,root) %{_libdir}/libcolorcorrect.so.*.*
%ghost %{_libdir}/libkfontinst.so.6
%attr(755,root,root) %{_libdir}/libkfontinst.so.*.*
%ghost %{_libdir}/libkfontinstui.so.6
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*.*
%ghost %{_libdir}/libkmpris.so.6
%attr(755,root,root) %{_libdir}/libkmpris.so.*.*
%ghost %{_libdir}/libkworkspace6.so.6
%attr(755,root,root) %{_libdir}/libkworkspace6.so.*.*
%ghost %{_libdir}/libnotificationmanager.so.1
%attr(755,root,root) %{_libdir}/libnotificationmanager.so.*.*
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*
%ghost %{_libdir}/libtaskmanager.so.6
%ghost %{_libdir}/libweather_ion.so.7
%attr(755,root,root) %{_libdir}/libweather_ion.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/appmenu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/colorcorrectlocationupdater.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/desktopnotifier.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/devicenotifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/freespacenotifier.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/ktimezoned.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/mprisservice.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/plasma-session-shortcuts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/plasma_accentcolor_service.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/soliduiserver.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/statusnotifierwatcher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/wallpaperfileitemaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/applications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/desktop.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_fonts.so
%dir %{_libdir}/qt6/plugins/kf6/krunner
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/calculator.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/helprunner.so
%dir %{_libdir}/qt6/plugins/kf6/krunner/kcms
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/kcms/kcm_krunner_kill.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_kill.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_placesrunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_recentdocuments.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_services.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_sessions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_shell.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/locations.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_layouttemplate.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/wallpaper_images.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/kfontviewpart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/fontthumbnail.so
%dir %{_libdir}/qt6/plugins/phonon_platform
%attr(755,root,root) %{_libdir}/qt6/plugins/phonon_platform/kde.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.appmenu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.calendar.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.icon.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.notifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.panelspacer.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.private.systemtray.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.systemmonitor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.systemtray.so
%dir %{_libdir}/qt6/plugins/plasma/containmentactions
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.applauncher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.contextmenu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.paste.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.switchdesktop.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/switchactivity.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/switchwindow.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcminit/kcm_fonts_init.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcminit/kcm_style_init.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_colors.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_icons.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_soundtheme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_style.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_users.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_wallpaper.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_applicationjobs.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_bbcukmet.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_clipboard.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_dwd.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_envcan.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_executable.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_noaa.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_notifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_time.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_weather.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_wettercom.so
%dir %{_libdir}/qt6/plugins/plasmacalendarplugins
%dir %{_libdir}/qt6/plugins/plasmacalendarplugins/holidays
%{_libdir}/qt6/plugins/plasmacalendarplugins/holidays/HolidaysConfig.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/ActionButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/Battery.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/Clock.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/RejectPasswordAnimation.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/RejectPasswordPathAnimation.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/SessionManagementScreen.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/UserDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/UserList.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/VirtualKeyboard.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/VirtualKeyboardLoader.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/VirtualKeyboard_wayland.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/WallpaperFader.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/components.qmltypes
%{_libdir}/qt6/qml/org/kde/breeze/components/kde-qmlmodule.version
%dir %{_libdir}/qt6/qml/org/kde/breeze/components
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/breeze/components/libcomponents.so
%{_libdir}/qt6/qml/org/kde/breeze/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/colorcorrect
%{_libdir}/qt6/qml/org/kde/colorcorrect/colorcorrect.qmltypes
%{_libdir}/qt6/qml/org/kde/colorcorrect/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/colorcorrect/libcolorcorrectplugin.so
%{_libdir}/qt6/qml/org/kde/colorcorrect/qmldir
%dir %{_libdir}/qt6/qml/org/kde/notificationmanager
%{_libdir}/qt6/qml/org/kde/notificationmanager/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/notificationmanager/libnotificationmanagerplugin.so
%{_libdir}/qt6/qml/org/kde/notificationmanager/notificationmanager.qmltypes
%{_libdir}/qt6/qml/org/kde/notificationmanager/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/lookandfeel
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/lookandfeel/liblookandfeelqmlplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/lookandfeel/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/appmenu
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/appmenu/libappmenuplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/appmenu/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/BasicAppletContainer.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/ConfigOverlayWithHandles.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/PlaceHolder.qml
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/libcontainmentlayoutmanagerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock/libdigitalclockplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/kicker
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/kicker/libkickerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/kicker/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mediacontroller
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mediacontroller/libmediacontrollerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mediacontroller/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mpris
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris/kmpris.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mpris/libkmprisplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/sessions
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/sessions/libsessionsprivateplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/sessions/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/shell
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/shell/libplasmashellprivateplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/shell/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/wallpapers
%dir %{_libdir}/qt6/qml/org/kde/plasma/wallpapers/image
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/wallpapers/image/libplasma_wallpaper_imageplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/wallpapers/image/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/DayDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/DaysCalendar.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/InfiniteList.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/MonthView.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/MonthViewHeader.qml
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/libcalendarplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/components
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/BadgeOverlay.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/BatteryIcon.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/KeyboardLayoutSwitcher.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/SystemDialog.qml
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/examples
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/examples/test.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/keyboardlayout
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/keyboardlayout/libkeyboardlayoutplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/keyboardlayout/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter/libtrianglemousefilterplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter/qmldir
%dir %{_libdir}/qt6/qml/org/kde/taskmanager
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/taskmanager/libtaskmanagerplugin.so
%{_libdir}/qt6/qml/org/kde/taskmanager/qmldir
%attr(755,root,root) %{_prefix}/libexec/baloorunner
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/fontinst
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/fontinst_helper
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/fontinst_x11
%attr(755,root,root) %{_prefix}/libexec/kfontprint
%attr(755,root,root) %{_prefix}/libexec/ksmserver-logout-greeter
%attr(755,root,root) %{_prefix}/libexec/plasma-changeicons
%attr(755,root,root) %{_prefix}/libexec/plasma-dbus-run-session-if-needed
%attr(755,root,root) %{_prefix}/libexec/plasma-sourceenv.sh
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasmashell-6.0-keep-custom-position-of-panels
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_appstream.so
%ghost %{_libdir}/libbatterycontrol.so.6
%attr(755,root,root) %{_libdir}/libbatterycontrol.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_nightlight.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasmacalendarplugins/holidaysevents.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/battery
%{_libdir}/qt6/qml/org/kde/plasma/private/battery/batterycontrol.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/battery/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/battery/libbatterycontrolplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/battery/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/BasicResizeHandle.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/containmentlayoutmanagerplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/kde-qmlmodule.version
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/devicenotifier
%{_libdir}/qt6/qml/org/kde/plasma/private/devicenotifier/devicenotifierplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/devicenotifier/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/devicenotifier/libdevicenotifierplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/devicenotifier/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock/digitalclockplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock/kde-qmlmodule.version
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/holidayevents
%{_libdir}/qt6/qml/org/kde/plasma/private/holidayevents/holidayevents.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/holidayevents/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/holidayevents/libholidayevents.so
%{_libdir}/qt6/qml/org/kde/plasma/private/holidayevents/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/keyboardindicator/kde-qmlmodule.version
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/keyboardindicator
%{_libdir}/qt6/qml/org/kde/plasma/private/keyboardindicator/keyboardindicatorplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/keyboardindicator/libkeyboardindicatorplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/keyboardindicator/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/sessions/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/sessions/sessionsprivateplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/systemtray
%{_libdir}/qt6/qml/org/kde/plasma/private/systemtray/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/systemtray/libsystemtrayplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/systemtray/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/systemtray/systemtrayplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/calendarplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/components/libworkspacecomponents.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/workspacecomponents.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dbus/dbusplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dbus/kde-qmlmodule.version
%dir %{_libdir}/qt6/qml/org/kde/plasma/workspace/dbus
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/dbus/libdbusplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dbus/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter/trianglemousefilterplugin.qmltypes
%attr(755,root,root) %{_prefix}/libexec/plasma-fallback-session-restore
%attr(755,root,root) %{_prefix}/libexec/plasma-fallback-session-save
%ghost %{_libdir}/libklipper.so.6
%attr(755,root,root) %{_libdir}/libklipper.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/donationmessage.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/clipboard
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/BarcodePage.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/ClipboardItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/ClipboardMenu.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/DelegateToolButtons.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/EditPage.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/ImageItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/KlipperPopup.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/TextItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/UrlItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/klipperplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/libklipperplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/clipboard/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/shell/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/shell/plasmashellprivateplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/taskmanager/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/taskmanager/taskmanager.qmltypes
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma6.3-update-clipboard-database-2-to-3
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/geotimezoned.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/oom-notifier.so

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/kcm_autostart.desktop
%{_desktopdir}/kcm_colors.desktop
%{_desktopdir}/kcm_cursortheme.desktop
%{_desktopdir}/kcm_desktoptheme.desktop
%{_desktopdir}/kcm_fontinst.desktop
%{_desktopdir}/kcm_fonts.desktop
%{_desktopdir}/kcm_icons.desktop
%{_desktopdir}/kcm_lookandfeel.desktop
%{_desktopdir}/kcm_notifications.desktop
%{_desktopdir}/kcm_regionandlang.desktop
%{_desktopdir}/kcm_soundtheme.desktop
%{_desktopdir}/kcm_style.desktop
%{_desktopdir}/kcm_users.desktop
%{_desktopdir}/kcm_wallpaper.desktop
%{_desktopdir}/org.kde.kcolorschemeeditor.desktop
%{_desktopdir}/org.kde.kfontview.desktop
%{_desktopdir}/org.kde.plasmashell.desktop
%{_desktopdir}/org.kde.plasmawindowed.desktop
%{_datadir}/config.kcfg/colorssettings.kcfg
%{_datadir}/config.kcfg/cursorthemesettings.kcfg
%{_datadir}/config.kcfg/fontssettings.kcfg
%{_datadir}/config.kcfg/freespacenotifier.kcfg
%{_datadir}/config.kcfg/iconssettingsbase.kcfg
%{_datadir}/config.kcfg/launchfeedbacksettings.kcfg
%{_datadir}/config.kcfg/lookandfeelsettings.kcfg
%{_datadir}/config.kcfg/stylesettings.kcfg
%{_datadir}/dbus-1/interfaces/com.canonical.AppMenu.Registrar.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSplash.xml
%{_datadir}/dbus-1/interfaces/org.kde.PlasmaShell.xml
%{_datadir}/dbus-1/interfaces/org.kde.kappmenu.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/org.kde.KSplash.service
%{_datadir}/dbus-1/services/org.kde.LogoutPrompt.service
%{_datadir}/dbus-1/services/org.kde.Shutdown.service
%{_datadir}/dbus-1/services/org.kde.fontinst.service
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/dbus-1/services/org.kde.plasma.Notifications.service
%{_datadir}/dbus-1/services/org.kde.runners.baloo.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%{_datadir}/desktop-directories/kf5-development-translation.directory
%{_datadir}/desktop-directories/kf5-development-webdevelopment.directory
%{_datadir}/desktop-directories/kf5-development.directory
%{_datadir}/desktop-directories/kf5-editors.directory
%{_datadir}/desktop-directories/kf5-edu-languages.directory
%{_datadir}/desktop-directories/kf5-edu-mathematics.directory
%{_datadir}/desktop-directories/kf5-edu-miscellaneous.directory
%{_datadir}/desktop-directories/kf5-edu-science.directory
%{_datadir}/desktop-directories/kf5-edu-tools.directory
%{_datadir}/desktop-directories/kf5-education.directory
%{_datadir}/desktop-directories/kf5-games-arcade.directory
%{_datadir}/desktop-directories/kf5-games-board.directory
%{_datadir}/desktop-directories/kf5-games-card.directory
%{_datadir}/desktop-directories/kf5-games-kids.directory
%{_datadir}/desktop-directories/kf5-games-logic.directory
%{_datadir}/desktop-directories/kf5-games-roguelikes.directory
%{_datadir}/desktop-directories/kf5-games-strategy.directory
%{_datadir}/desktop-directories/kf5-games.directory
%{_datadir}/desktop-directories/kf5-graphics.directory
%{_datadir}/desktop-directories/kf5-internet-terminal.directory
%{_datadir}/desktop-directories/kf5-internet.directory
%{_datadir}/desktop-directories/kf5-main.directory
%{_datadir}/desktop-directories/kf5-more.directory
%{_datadir}/desktop-directories/kf5-multimedia.directory
%{_datadir}/desktop-directories/kf5-network.directory
%{_datadir}/desktop-directories/kf5-office.directory
%{_datadir}/desktop-directories/kf5-science.directory
%{_datadir}/desktop-directories/kf5-settingsmenu.directory
%{_datadir}/desktop-directories/kf5-system-terminal.directory
%{_datadir}/desktop-directories/kf5-system.directory
%{_datadir}/desktop-directories/kf5-toys.directory
%{_datadir}/desktop-directories/kf5-unknown.directory
%{_datadir}/desktop-directories/kf5-utilities-accessibility.directory
%{_datadir}/desktop-directories/kf5-utilities-desktop.directory
%{_datadir}/desktop-directories/kf5-utilities-file.directory
%{_datadir}/desktop-directories/kf5-utilities-peripherals.directory
%{_datadir}/desktop-directories/kf5-utilities-pim.directory
%{_datadir}/desktop-directories/kf5-utilities-xutils.directory
%{_datadir}/desktop-directories/kf5-utilities.directory
%{_iconsdir}/hicolor/128x128/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/16x16/apps/kfontview.png
%{_iconsdir}/hicolor/16x16/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/22x22/apps/kfontview.png
%{_iconsdir}/hicolor/22x22/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/32x32/apps/kfontview.png
%{_iconsdir}/hicolor/32x32/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/48x48/apps/kfontview.png
%{_iconsdir}/hicolor/48x48/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/64x64/apps/kfontview.png
%{_iconsdir}/hicolor/64x64/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%attr(755,root,root) %{_datadir}/kconf_update/migrate-calendar-to-plugin-id.py
%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.upd
%{_datadir}/kconf_update/plasma6.0-remove-dpi-settings.upd
%{_datadir}/kconf_update/plasma6.0-remove-old-shortcuts.upd
%{_datadir}/kconf_update/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels.upd
%dir %{_datadir}/kfontinst
%dir %{_datadir}/kfontinst/icons
%dir %{_datadir}/kfontinst/icons/hicolor
%dir %{_datadir}/kfontinst/icons/hicolor/16x16
%dir %{_datadir}/kfontinst/icons/hicolor/16x16/actions
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/font-disable.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/font-enable.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/fontstatus.png
%dir %{_datadir}/kfontinst/icons/hicolor/22x22
%dir %{_datadir}/kfontinst/icons/hicolor/22x22/actions
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/font-disable.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/font-enable.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/fontstatus.png
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/kio/servicemenus/installfont.desktop
%dir %{_datadir}/kio_desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash
%{_datadir}/knotifications6/devicenotifications.notifyrc
%{_datadir}/knotifications6/freespacenotifier.notifyrc
%{_datadir}/knotifications6/phonon.notifyrc
%{_datadir}/knsrcfiles/colorschemes.knsrc
%{_datadir}/knsrcfiles/gtk_themes.knsrc
%{_datadir}/knsrcfiles/icons.knsrc
%{_datadir}/knsrcfiles/kfontinst.knsrc
%{_datadir}/knsrcfiles/lookandfeel.knsrc
%{_datadir}/knsrcfiles/plasma-themes.knsrc
%{_datadir}/knsrcfiles/plasmoids.knsrc
%{_datadir}/knsrcfiles/wallpaper-mobile.knsrc
%{_datadir}/knsrcfiles/wallpaper.knsrc
%{_datadir}/knsrcfiles/wallpaperplugin.knsrc
%{_datadir}/knsrcfiles/xcursor.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kstyle/themes/qtcde.themerc
%{_datadir}/kstyle/themes/qtcleanlooks.themerc
%{_datadir}/kstyle/themes/qtgtk.themerc
%{_datadir}/kstyle/themes/qtmotif.themerc
%{_datadir}/kstyle/themes/qtplastique.themerc
%{_datadir}/kstyle/themes/qtwindows.themerc
%dir %{_datadir}/kxmlgui5/kfontview
%{_datadir}/kxmlgui5/kfontview/kfontviewpart.rc
%{_datadir}/kxmlgui5/kfontview/kfontviewui.rc
%{_datadir}/metainfo/org.kde.breeze.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezedark.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezetwilight.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.color.appdata.xml
%{_datadir}/metainfo/org.kde.image.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.activitybar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.analogclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.appmenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.calendar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.cameraindicator.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.clipboard.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.devicenotifier.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.digitalclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.lock_logout.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.manage-inputmethod.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mediacontroller.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.notifications.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpucore.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.diskactivity.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.diskusage.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.memory.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.net.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemtray.appdata.xml
%{_datadir}/metainfo/org.kde.slideshow.appdata.xml
%{_datadir}/plasma/avatars
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/defaults
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/layouts
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/Logout.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/LogoutButton.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/timer.js
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd/Osd.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd/OsdItem.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/lockscreen.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/splash.png
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/Splash.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/busywidget.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/kde.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/plasma.svgz
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/systemdialog
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/systemdialog/SystemDialog.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/metadata.json
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/layouts
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.json
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/defaults
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/layouts
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%dir %{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/previews
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/Hand.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/MenuDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images/mini-calendar.svgz
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/DeviceItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/CalendarView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/DigitalClock.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/Tooltip.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configCalendar.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configTimeZones.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/data.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/AlbumArtStackView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/ExpandedRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/DraggableDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationPopup.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/Globals.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/PulseAudio.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/qmldir
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/applet
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/applet/CompactApplet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ConfigEntries.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/CurrentItemHighLight.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ExpandedRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ExpanderArrow.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/HiddenItemsView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/PlasmoidPopupsContainer.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/SystemTrayState.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/AbstractItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/ItemLoader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/PlasmoidItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/PulseAnimation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/StatusNotifierItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/ConfigSensors.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/FaceDetails.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.color
%dir %{_datadir}/plasma/wallpapers/org.kde.color/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.color/contents/config
%{_datadir}/plasma/wallpapers/org.kde.color/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.color/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.color/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.color/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.color/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.image
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/config
%{_datadir}/plasma/wallpapers/org.kde.image/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/AddFileDialog.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/ImageStackView.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/ThumbnailsComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/main.qml
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/AnimatedImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/BaseMediaComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/BlurComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/StaticImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/AddFileDialog.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/ImageStackView.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/SlideshowComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/ThumbnailsComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/main.qml
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/AnimatedImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/BaseMediaComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/BlurComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/StaticImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/metadata.json
%{_datadir}/plasma5support/services/applicationjobs.operations
%{_datadir}/plasma5support/services/notifications.operations
%{_datadir}/plasma5support/services/org.kde.plasma.clipboard.operations
%{_datadir}/plasma5support/services/statusnotifieritem.operations
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_datadir}/qlogging-categories6/kcm_regionandlang.categories
%{_datadir}/qlogging-categories6/kcmusers.categories
%{_datadir}/qlogging-categories6/klipper.categories
%{_datadir}/qlogging-categories6/libnotificationmanager.categories
%{_datadir}/qlogging-categories6/plasma-workspace.categories
%{_datadir}/solid/actions/openWithFileManager.desktop
%{_datadir}/wayland-sessions/plasma.desktop
%{_datadir}/xsessions/plasmax11.desktop
%{zsh_compdir}/_krunner
%{zsh_compdir}/_plasmashell
%{_datadir}/kconf_update/plasmashell-6.0-keep-custom-position-of-panels.upd
%dir %{_datadir}/plasma/weather
%{_datadir}/plasma/weather/noaa_station_list.xml
%{_datadir}/qlogging-categories6/batterycontrol.categories
%{_desktopdir}/kcm_nightlight.desktop
%{_desktopdir}/org.kde.kfontinst.desktop
%{_desktopdir}/org.kde.plasma-fallback-session-save.desktop
%{_datadir}/metainfo/org.kde.plasma.panelspacer.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/main.qml
%{_datadir}/qlogging-categories6/devicenotifier.categories
%{_datadir}/xdg-desktop-portal/kde-portals.conf
%{_datadir}/knotifications6/donationmessage.notifyrc
%{_desktopdir}/org.kde.klipper.desktop
%{_datadir}/desktop-directories/kf5-help.directory
%{_datadir}/kconf_update/plasma6.3-update-clipboard-database-2-to-3.upd
%{_datadir}/knotifications6/libnotificationmanager.notifyrc
%{_datadir}/knotifications6/oom-notifier.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/NoTimezoneWarning.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/ActionContainer.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/Body.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/DraggableFileArea.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/EditContextMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/FooterLoader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/HeadingButtons.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/Icon.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/JobDetails.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/JobIconItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/JobItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/ModelInterface.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/NotificationHeader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/NotificationReplyField.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/Summary.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/components/ThumbnailStrip.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/delegates
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/delegates/BaseDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/delegates/DelegateHistory.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/delegates/DelegateHistoryGrouped.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/delegates/DelegatePopup.qml

%files devel
%defattr(644,root,root,755)
%{_includedir}/krdb
%{_includedir}/kworkspace6
%{_includedir}/plasma5support
%{_includedir}/taskmanager
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/libtaskmanager.so
%{_libdir}/libweather_ion.so
%{_includedir}/colorcorrect
%{_libdir}/cmake/LibColorCorrect
%{_libdir}/libcolorcorrect.so
%{_includedir}/notificationmanager
%{_libdir}/cmake/LibNotificationManager
%{_libdir}/libkfontinst.so
%{_libdir}/libkfontinstui.so
%{_libdir}/libnotificationmanager.so
%{_libdir}/libkrdb.so
%{_libdir}/libkworkspace6.so
%{_libdir}/libbatterycontrol.so
%{_libdir}/libklipper.so
