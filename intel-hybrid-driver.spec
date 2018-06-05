#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-hybrid-driver
Version  : 1.0.2
Release  : 6
URL      : https://github.com/01org/intel-hybrid-driver/archive/1.0.2.tar.gz
Source0  : https://github.com/01org/intel-hybrid-driver/archive/1.0.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Distributable MIT
Requires: intel-hybrid-driver-lib
Requires: cmrt
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(intel-gen4asm)
BuildRequires : pkgconfig(libcmrt)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(wayland-client)
Patch1: 0001-driver_init-load-libva-x11.so-for-any-ABI-version.patch

%description
libva-intel-hybrid-driver
VA driver for Intel G45 & HD Graphics family
License
-------
Please read the COPYING file available in this package.

%package lib
Summary: lib components for the intel-hybrid-driver package.
Group: Libraries

%description lib
lib components for the intel-hybrid-driver package.


%prep
%setup -q -n intel-hybrid-driver-1.0.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528221105
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1528221105
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/hybrid_drv_video.so
