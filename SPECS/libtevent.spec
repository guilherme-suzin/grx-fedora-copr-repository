Name:           libtevent
Version:        0.17.1
Release:        100%{?dist}
Summary:        The tevent event library
License:        LGPL-3.0-or-later
URL:            https://tevent.samba.org/
Source0:        tevent-%{version}.tar.gz

# Versão mínima do talloc usada pelos fontes Samba
%global talloc_version 2.4.3

# Build deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  libtalloc-devel >= %{talloc_version}
BuildRequires:  libcmocka-devel >= 1.1.3
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  doxygen

Provides:       bundled(libreplace)

%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provides helpers to deal with asynchronous code via tevent_req
(Tevent Request) functions.

# ----------------------------------------------------------------------
# -devel
# ----------------------------------------------------------------------
%package devel
Summary:        Developer files for the Tevent library
Requires:       libtevent%{?_isa} = %{version}-%{release}
Requires:       libtalloc-devel%{?_isa} >= %{talloc_version}

%description devel
Header files and pkgconfig file needed to develop programs that
link against the Tevent library.

# ----------------------------------------------------------------------
# PREP
# ----------------------------------------------------------------------
%prep
%setup -q -n tevent-%{version}

# ----------------------------------------------------------------------
# BUILD
# ----------------------------------------------------------------------
%build
# Só lib C; sem bindings Python
%configure \
    --disable-rpath \
    --bundled-libraries=NONE \
    --builtin-libraries=replace \
    --disable-python

%make_build

# Documentação API (doxygen)
doxygen doxy.config

# ----------------------------------------------------------------------
# TESTS
# ----------------------------------------------------------------------
%check
# Testes Python de bindings não fazem sentido sem _tevent, então pulamos o check
# make check

# ----------------------------------------------------------------------
# INSTALL
# ----------------------------------------------------------------------
%install
%make_install

# Instala manpages
rm -f doc/man/man3/todo*
install -d -m0755 %{buildroot}%{_mandir}
cp -a doc/man/man3 %{buildroot}%{_mandir}

# ----------------------------------------------------------------------
# FILES
# ----------------------------------------------------------------------
%files
%license LICENSE
%{_libdir}/libtevent.so.*

%files devel
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc
%{_mandir}/man3/tevent*.gz

%ldconfig_scriptlets

%changelog
* Thu Nov 27 2025 Guilherme / Onbit <you@example.com> - 0.17.1-100
- Repackaged libtevent 0.17.1 for EL10 (Rocky/Alma/CentOS Stream)
- Build only C library and -devel, without Python bindings or Python tests
