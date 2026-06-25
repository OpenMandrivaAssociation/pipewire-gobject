%define __name pwg
%define libname %mklibname pipewire-gobject
%define devname %mklibname -d pipewire-gobject
%define girname %mklibname pipewire-gobject-gir
%define namespace Pwg
%define api_ver 0.1

%def_enable tests
%def_enable check

Name: pipewire-gobject
Version: 0.3.9
Release: 1
Summary: Experimental GObject/GObject-Introspection binding layer for PipeWire
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/bhack/pipewire-gobject
Source0: https://github.com/bhack/pipewire-gobject/archive/%{version}/%{name}-%{version}.tar.gz


%define pw_api_ver 0.3

BuildRequires: meson 
BuildRequires: gi-docgen
BuildRequires: gobject-introspection
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(glib-2.0)

%description
This project is a prototype for exposing a safe, high-level, app-facing
PipeWire API to Python, GJS, Vala, and other GI consumers. It is not a
complete PipeWire binding yet, and it is not a mechanical one-to-one
binding of the C API.

%package -n %{libname}
Summary: %name shared library
Group: System/Libraries
Requires: python-gobject3
Requires: %{_lib}pipewire
Requires: typelib(GIRepository)

%description -n %{libname}
This package provides shared %namespace library.

%package -n %{devname}
Summary: Development files for %libname
Group: Development/C
Requires: %{libname} = %EVR

%description -n %{devname}
The %libname-devel package provides libraries and header files for
developing applications that use %namespace library.

%package -n %{girname}
Summary: GObject introspection data for %_name
Group: System/Libraries
Requires: %{libname} = %EVR

%description -n %{girname}
GObject introspection data for %_name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name.

%package examples
Summary: simple applications from %_name package
Group: Development/Other
Requires: %{girname} = %EVR

%description examples
This package provides example programs that can be used to chek
the functionality of the %_name library.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson \
%meson_build

%install
%meson_install

%files -n %{libname}
%_libdir/%libname-%api_ver.so.*
%doc AGENTS* CHANGELOG* README*

%files -n %files -n %{devname}
%_includedir/%__name-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%__name-%api_ver.pc
%{_datadir}/gir-1.0/%namespace-%api_ver.gir

%files -n %{girname}
%_typelibdir/%namespace-%api_ver.typelib

%if_enabled doc
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif
