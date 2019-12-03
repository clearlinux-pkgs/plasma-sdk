#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-sdk
Version  : 5.17.4
Release  : 29
URL      : https://download.kde.org/stable/plasma/5.17.4/plasma-sdk-5.17.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.17.4/plasma-sdk-5.17.4.tar.xz
Source1 : https://download.kde.org/stable/plasma/5.17.4/plasma-sdk-5.17.4.tar.xz.sig
Summary  : Applications useful for Plasma development
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: plasma-sdk-bin = %{version}-%{release}
Requires: plasma-sdk-data = %{version}-%{release}
Requires: plasma-sdk-lib = %{version}-%{release}
Requires: plasma-sdk-license = %{version}-%{release}
Requires: plasma-sdk-locales = %{version}-%{release}
Requires: plasma-sdk-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kirigami2-dev
BuildRequires : ktexteditor-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the plasma-sdk package.
Group: Binaries
Requires: plasma-sdk-data = %{version}-%{release}
Requires: plasma-sdk-license = %{version}-%{release}

%description bin
bin components for the plasma-sdk package.


%package data
Summary: data components for the plasma-sdk package.
Group: Data

%description data
data components for the plasma-sdk package.


%package lib
Summary: lib components for the plasma-sdk package.
Group: Libraries
Requires: plasma-sdk-data = %{version}-%{release}
Requires: plasma-sdk-license = %{version}-%{release}

%description lib
lib components for the plasma-sdk package.


%package license
Summary: license components for the plasma-sdk package.
Group: Default

%description license
license components for the plasma-sdk package.


%package locales
Summary: locales components for the plasma-sdk package.
Group: Default

%description locales
locales components for the plasma-sdk package.


%package man
Summary: man components for the plasma-sdk package.
Group: Default

%description man
man components for the plasma-sdk package.


%prep
%setup -q -n plasma-sdk-5.17.4
cd %{_builddir}/plasma-sdk-5.17.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575386633
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1575386633
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-sdk
cp %{_builddir}/plasma-sdk-5.17.4/COPYING %{buildroot}/usr/share/package-licenses/plasma-sdk/579588a75aec3d4f0d4629a074965f459f4e2504
cp %{_builddir}/plasma-sdk-5.17.4/COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-sdk/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang cuttlefish
%find_lang cuttlefish_editorplugin
%find_lang org.kde.plasma.lookandfeelexplorer
%find_lang org.kde.plasma.themeexplorer
%find_lang plasma_shell_org.kde.plasmoidviewershell
%find_lang plasmaengineexplorer
%find_lang plasmawallpaperviewer
%find_lang plasmoidviewer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cuttlefish
/usr/bin/lookandfeelexplorer
/usr/bin/plasmaengineexplorer
/usr/bin/plasmathemeexplorer
/usr/bin/plasmoidviewer

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.cuttlefish.desktop
/usr/share/applications/org.kde.plasma.lookandfeelexplorer.desktop
/usr/share/applications/org.kde.plasma.themeexplorer.desktop
/usr/share/applications/org.kde.plasmaengineexplorer.desktop
/usr/share/applications/org.kde.plasmoidviewer.desktop
/usr/share/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/FormField.qml
/usr/share/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/FormLabel.qml
/usr/share/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/MetadataEditor.qml
/usr/share/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/main.qml
/usr/share/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/metadata.desktop
/usr/share/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/metadata.json
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/code/openInEditor.sh
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/data/themeDescription.json
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/data/todo
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/ColorButton.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/ColorEditor.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/FormLabel.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/MetadataEditor.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/Hand.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/actionbutton.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/allframesvgs.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/analog_meter.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/busyindicator.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/button.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/checkmarks.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/clock.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/containment-controls.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/dialog.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/framesvg.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/icons.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/listitem.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/monitor.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/panel.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/progressbar.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/scrollbar.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/slider.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/tabbar.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/textfield.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols/Button.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols/CheckBox.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols/LineEdit.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/main.qml
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/metadata.desktop
/usr/share/kpackage/genericqml/org.kde.plasma.themeexplorer/metadata.json
/usr/share/kservices5/plasma-package-org.kde.plasma.cuttlefish.desktop
/usr/share/kservices5/plasma-shell-org.kde.plasma.plasmoidviewershell.desktop
/usr/share/metainfo/org.kde.cuttlefish.appdata.xml
/usr/share/metainfo/org.kde.plasma.cuttlefish.appdata.xml
/usr/share/metainfo/org.kde.plasma.lookandfeelexplorer.appdata.xml
/usr/share/metainfo/org.kde.plasma.plasmoidviewershell.appdata.xml
/usr/share/metainfo/org.kde.plasma.themeexplorer.appdata.xml
/usr/share/metainfo/org.kde.plasmaengineexplorer.appdata.xml
/usr/share/metainfo/org.kde.plasmoidviewer.appdata.xml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/DualMontage.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/GlobalMenuBar.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/IconGrid.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/IconGridDelegate.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/Menu.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/Preview.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/ResponsivePreview.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/SvgGrid.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/Tools.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/ToolsResponsive.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/cuttlefish.qml
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/metadata.desktop
/usr/share/plasma/packages/org.kde.plasma.cuttlefish/metadata.json
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet/AppletError.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet/CompactApplet.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet/DefaultCompactRepresentation.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/AppletConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigCategoryDelegate.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationContainmentActions.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationContainmentAppearance.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationKcmPage.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationShortcuts.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ContainmentConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/MouseEventInputButton.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/PanelConfiguration.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/defaults
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/Background.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/Desktop.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/Konsole.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/SdkButtons.qml
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/metadata.desktop
/usr/share/plasma/shells/org.kde.plasma.plasmoidviewershell/metadata.json

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/ktexteditor/cuttlefishplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-sdk/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/plasma-sdk/579588a75aec3d4f0d4629a074965f459f4e2504

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/plasmaengineexplorer.1
/usr/share/man/man1/plasmoidviewer.1

%files locales -f cuttlefish.lang -f cuttlefish_editorplugin.lang -f org.kde.plasma.lookandfeelexplorer.lang -f org.kde.plasma.themeexplorer.lang -f plasma_shell_org.kde.plasmoidviewershell.lang -f plasmaengineexplorer.lang -f plasmawallpaperviewer.lang -f plasmoidviewer.lang
%defattr(-,root,root,-)

