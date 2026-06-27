%define libname %mklibname pipewire-gobject
%define devname %mklibname -d pipewire-gobject
%define girname %mklibname pipewire-gobject-gir
%define api 0.1
%define major 0

Name: pipewire-gobject
Version: 0.3.9
Release: 1
Summary: Experimental GObject/GObject-Introspection binding layer for PipeWire
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/bhack/pipewire-gobject
Source0: https://github.com/bhack/pipewire-gobject/archive/%{version}/%{name}-%{version}.tar.gz

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
Summary: %{name} shared library
Group: System/Libraries
Requires: python-gobject3
Requires: %{_lib}pipewire
Requires: typelib(GIRepository)

%description -n %{libname}
This package provides shared %{name} library.

%package -n %{devname}
Summary: Development files for %{libname}
Group: Development/C
Provides: %{name}-devel = %{EVRD}
Requires: %{libname} = %{EVRD}

%description -n %{devname}
The %{libname}-devel package provides libraries and header files for
developing applications that use %{name} library.

%package -n %{girname}
Summary: GObject introspection data for %{name}
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{girname}
GObject introspection data for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson \
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libpwg-%{api}.so.%{major}*
%doc AGENTS* CHANGELOG* README*

%files -n %{devname}
%{_includedir}/pwg-%{api}/pwg/
%{_libdir}/libpwg-%{api}.so
%{_libdir}/pkgconfig/pwg-%{api}.pc
%{_datadir}/gir-1.0/Pwg-%{api}.gir

%files -n %{girname}
%{_libdir}/girepository-1.0/Pwg-%{api}.typelib
