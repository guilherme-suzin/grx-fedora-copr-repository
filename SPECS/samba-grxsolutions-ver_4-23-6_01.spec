Name:           samba
Version:        4.23.6
Release:        1%{?dist}
Summary:        Server and client for SMB/CIFS and Active Directory
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.samba.org
Source0:        %{name}-%{version}.tar.gz

# ==== Build feature toggles ===============================================
%bcond_without ad_dc
%bcond_without cups
%bcond_without pam
%bcond_without snapper
%bcond_with    check

# ==== BuildRequires ========================================================

BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  avahi-devel
BuildRequires:  bash
BuildRequires:  bind-utils
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  cargo
BuildRequires:  ccache
BuildRequires:  chrpath
BuildRequires:  clang-devel
BuildRequires:  crypto-policies-scripts
BuildRequires:  cups-devel
BuildRequires:  curl
BuildRequires:  dbus
BuildRequires:  dbus-devel
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  glibc-common
BuildRequires:  glibc-langpack-en
BuildRequires:  gnutls-devel
BuildRequires:  gnutls-utils
BuildRequires:  gpgme-devel
BuildRequires:  gzip
BuildRequires:  hostname
BuildRequires:  jansson-devel
BuildRequires:  jq
BuildRequires:  keyutils-libs-devel
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  krb5-workstation
BuildRequires:  ldb-tools
BuildRequires:  libacl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libattr-devel
BuildRequires:  libblkid-devel
BuildRequires:  libbsd-devel
BuildRequires:  libcap-devel
BuildRequires:  libevent-devel
BuildRequires:  libicu-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtasn1-tools
BuildRequires:  libtirpc-devel
BuildRequires:  libtalloc
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent
BuildRequires:  libtevent-devel
BuildRequires:  libunwind-devel
BuildRequires:  liburing-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  lmdb
BuildRequires:  lmdb-devel
BuildRequires:  lsb_release
BuildRequires:  make
BuildRequires:  mingw64-gcc
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  patch
BuildRequires:  perl
BuildRequires:  perl-Archive-Tar
BuildRequires:  perl-ExtUtils-MakeMaker
BuildRequires:  perl-File-Compare
BuildRequires:  perl-Parse-Yapp
BuildRequires:  perl-Test-Simple
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf
BuildRequires:  pkgconf-m4
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  procps-ng
BuildRequires:  psmisc
BuildRequires:  python3
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-dns
BuildRequires:  python3-gpg
BuildRequires:  python3-iso8601
BuildRequires:  python3-libsemanage
BuildRequires:  python3-markdown
BuildRequires:  python3-policycoreutils
BuildRequires:  python3-pyasn1
BuildRequires:  python3-requests
BuildRequires:  python3-setproctitle
BuildRequires:  python3-talloc
BuildRequires:  python3-tdb
BuildRequires:  python3-tevent
BuildRequires:  python3-ldb
BuildRequires:  quota-devel
BuildRequires:  readline-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  rng-tools
BuildRequires:  rpcgen
BuildRequires:  rpcsvc-proto-devel
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  sudo
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar
BuildRequires:  tracker-devel
BuildRequires:  tree
BuildRequires:  utf8proc-devel
BuildRequires:  wget
BuildRequires:  which
BuildRequires:  xfsprogs-devel
BuildRequires:  xz
BuildRequires:  yum-utils
BuildRequires:  zlib-devel

%if %{with snapper}
BuildRequires:  dbus
BuildRequires:  dbus-devel
%endif

%if %{with check}
BuildRequires:  bash
BuildRequires:  python3-iso8601
BuildRequires:  python3-cryptography
BuildRequires:  python3-pyasn1
%endif

# ==== Runtime base =========================================================
Requires:       acl
Requires:       attr
Requires:       cups
Requires:       dbus-libs
Requires:       flex
Requires:       gnutls >= 3.4.7
Requires:       gpgme
Requires:       jansson
Requires:       krb5-libs
Requires:       krb5-workstation
Requires:       libacl
Requires:       libaio
Requires:       libarchive
Requires:       libattr
Requires:       libblkid
Requires:       libbsd
Requires:       libtasn1
Requires:       libtasn1-tools
Requires:       libxml2
Requires:       libxslt
Requires:       lmdb
Requires:       openldap
Requires:       pam
Requires:       patch
Requires:       perl
Requires:       perl-ExtUtils-MakeMaker
Requires:       perl-Parse-Yapp
Requires:       popt
Requires:       python3
Requires:       python3-cryptography
Requires:       python3-dns
Requires:       python3-gpg
Requires:       python3-iso8601
Requires:       python3-libsemanage
Requires:       python3-markdown
Requires:       python3-policycoreutils
Requires:       python3-pyasn1
Requires:       python3-requests
Requires:       python3-setproctitle
Requires:       readline
Requires:       rpcgen
Requires:       systemd
Requires:       tar
Requires:       zlib

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

# ==== Base/meta package ====================================================

Provides:       samba-common = %{version}-%{release}
Provides:       samba-common-libs = %{version}-%{release}
Provides:       samba-client-libs = %{version}-%{release}
Provides:       libwbclient = %{version}-%{release}

Conflicts:      samba
Conflicts:      samba-common
Conflicts:      samba-common-libs
Conflicts:      samba-client-libs
Conflicts:      libwbclient

Obsoletes:      samba < %{version}-%{release}
Obsoletes:      samba-common < %{version}-%{release}
Obsoletes:      samba-common-libs < %{version}-%{release}
Obsoletes:      samba-client-libs < %{version}-%{release}
Obsoletes:      libwbclient < %{version}-%{release}

Requires:       samba-dc = %{version}-%{release}

%description
Samba provides SMB/CIFS file and print services and can act as an Active Directory
domain controller. Several utilities (e.g. samba-tool) and the build system are
written in Python 3.x.

# ==== samba-dc =============================================================

%package dc
Summary:        Samba Active Directory Domain Controller
Provides:       samba-dc = %{version}-%{release}
Obsoletes:      samba-dc < %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description dc
Active Directory Domain Controller binaries, state directories and systemd unit
for Samba.

# ==== samba-ldb-tools ======================================================

%package ldb-tools
Summary:        LDB command line tools bundled with Samba
Provides:       ldb-tools = %{version}-%{release}
Conflicts:      ldb-tools
Obsoletes:      ldb-tools < %{version}-%{release}
# Rocky 9: também substitui a libldb da distro, pois os módulos em
# /usr/lib64/samba/ldb/*.so entram em conflito com o pacote libldb.
Provides:       libldb = %{version}-%{release}
Conflicts:      libldb
Obsoletes:      libldb < %{version}-%{release}

%description ldb-tools
LDB administration tools and LDB Samba modules bundled with this Samba build.

%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=/usr \
   --exec-prefix=/usr \
   --libdir=%{_libdir} \
   --libexecdir=%{_libexecdir} \
   --sbindir=%{_sbindir} \
   --sysconfdir=/etc \
   --localstatedir=/var \
   --mandir=/usr/share/man \
   --with-lockdir=/var/lib/samba \
   --with-piddir=/run/samba \
   --with-logfilebase=/var/log/samba \
   --enable-fhs \
   --bundled-libraries=cmocka

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Diretórios de estado/runtime corretos
install -d %{buildroot}/var/lib/samba
install -d %{buildroot}/var/lib/samba/private
install -d %{buildroot}/var/cache/samba
install -d %{buildroot}/var/log/samba
install -d %{buildroot}/run/samba

# NÃO REMOVER libs privadas do Samba / LDB, pois são necessárias.
# Apenas remover manpage de talloc (conflito com libtalloc-devel do sistema)
rm -f %{buildroot}%{_mandir}/man3/talloc.3* || true

# Unidade systemd AD DC
install -d %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/samba-ad-dc.service << 'EOF'
[Unit]
Description=Samba Active Directory Domain Controller
Documentation=man:samba(8) man:samba-tool(8)
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/sbin/samba -F
TimeoutStartSec=300
LimitNOFILE=16384
Environment=KRB5_KTNAME=/var/lib/samba/private/krb5.keytab
KillMode=process

[Install]
WantedBy=multi-user.target
EOF

# --- Manifesto do pacote base/meta ----------------------------------------
# Mantém apenas configs base, docs e alguns arquivos genéricos.
find %{buildroot} -mindepth 1 \( -type f -o -type l -o -type d \) \
   | sed "s|^%{buildroot}||" \
   | grep -vE '^/$|^/usr$|^/usr/bin$|^/usr/sbin$|^/usr/lib$|^/usr/lib64$' \
   | grep -vE '^/usr/lib/debug/|^/usr/lib/.build-id/' \
   | grep -vE '^%{_unitdir}/samba-ad-dc.service$' \
   | grep -vE '^/var/lib/samba($|/)' \
   | grep -vE '^/var/cache/samba($|/)' \
   | grep -vE '^/var/log/samba($|/)' \
   | grep -vE '^/run/samba($|/)' \
   | grep -vE '^%{_bindir}/ldb(add|del|edit|modify|rename|search)$' \
   | grep -vE '^%{_mandir}/man1/ldb(add|del|edit|modify|rename|search)\.1.*$' \
   | grep -vE '^/usr/lib64/samba/ldb($|/)' \
   | sort -u > %{_builddir}/filelist.base

# --- Manifesto do samba-dc -------------------------------------------------
(
  [ -x %{buildroot}%{_sbindir}/samba ] && echo %{_sbindir}/samba
  [ -x %{buildroot}%{_bindir}/samba-tool ] && echo %{_bindir}/samba-tool
  [ -f %{buildroot}%{_unitdir}/samba-ad-dc.service ] && echo %{_unitdir}/samba-ad-dc.service
  [ -d %{buildroot}/var/lib/samba ] && echo /var/lib/samba
  [ -d %{buildroot}/var/lib/samba/private ] && echo /var/lib/samba/private
  [ -d %{buildroot}/var/cache/samba ] && echo /var/cache/samba
  [ -d %{buildroot}/var/log/samba ] && echo /var/log/samba
  [ -d %{buildroot}/run/samba ] && echo /run/samba
) | sort -u > %{_builddir}/filelist.dc

# --- Manifesto do samba-ldb-tools -----------------------------------------
(
  for f in \
    %{_bindir}/ldbadd \
    %{_bindir}/ldbdel \
    %{_bindir}/ldbedit \
    %{_bindir}/ldbmodify \
    %{_bindir}/ldbrename \
    %{_bindir}/ldbsearch \
    %{_mandir}/man1/ldbadd.1* \
    %{_mandir}/man1/ldbdel.1* \
    %{_mandir}/man1/ldbedit.1* \
    %{_mandir}/man1/ldbmodify.1* \
    %{_mandir}/man1/ldbrename.1* \
    %{_mandir}/man1/ldbsearch.1*
  do
    ls %{buildroot}$f 2>/dev/null | sed "s|^%{buildroot}||"
  done

  if [ -d %{buildroot}/usr/lib64/samba/ldb ]; then
      echo /usr/lib64/samba/ldb
      find %{buildroot}/usr/lib64/samba/ldb -mindepth 1 \( -type f -o -type l -o -type d \) \
         | sed "s|^%{buildroot}||"
  fi

  for f in \
    /usr/lib64/samba/libldb-key-value-private-samba.so \
    /usr/lib64/samba/libldb-mdb-int-private-samba.so \
    /usr/lib64/samba/libldb-tdb-err-map-private-samba.so \
    /usr/lib64/samba/libldb-tdb-int-private-samba.so \
    /usr/lib64/samba/libldb-cmdline-private-samba.so
  do
    [ -e %{buildroot}$f ] && echo $f
  done
) | sort -u > %{_builddir}/filelist.ldbtools

%post
# Cria smb.conf padrão somente na primeira instalação.
if [ ! -f %{_sysconfdir}/samba/smb.conf ]; then
   mkdir -p %{_sysconfdir}/samba
   cat > %{_sysconfdir}/samba/smb.conf <<'EOF'
[global]
    workgroup = TESTE
    realm = TESTE.NET
    netbios name = SERVER
    server string = Domain Controller (DC) TESTE.NET - Samba %v
    server role = active directory domain controller
    disable netbios = yes
    smb ports = 445
    dns proxy = no
    server min protocol = SMB3

    # === Configurações de Log e Desempenho (Padrão) ===
    log file = /var/log/samba/log.%m
    max log size = 10000
    log level = 3

    # Otimização de I/O
    use sendfile = yes
    aio read size = 1024
    aio write size = 1024

    # homes = /home/%U
    # read only = no
EOF
fi

%post dc
%systemd_post samba-ad-dc.service

%preun dc
%systemd_preun samba-ad-dc.service

%postun dc
%systemd_postun_with_restart samba-ad-dc.service

%check
%if %{with check}
true
%endif

# ====================================================================
# Pacote principal/meta
# ====================================================================

%files -f %{_builddir}/filelist.base
%license COPYING
%doc README*
%dir %{_sysconfdir}/samba
%config(noreplace) %ghost %{_sysconfdir}/samba/smb.conf

# ====================================================================
# Pacote samba-dc
# ====================================================================

%files dc -f %{_builddir}/filelist.dc

# ====================================================================
# Pacote samba-ldb-tools
# ====================================================================

%files ldb-tools -f %{_builddir}/filelist.ldbtools

%changelog
* Fri Mar 06 2026 Guilherme Suzin <gui.suzin@live.com> - 4.23.6-1
- Update to Samba 4.23.6
- Includes upstream maintenance updates from 4.23.4, 4.23.5 and 4.23.6
- Fixes for winbind cache consistency
- Fixes for macOS Spotlight (mdssvc) integration
- Fixes for VFS stability issues
- Fixes for CTDB cluster lock configuration crash scenarios
- General bugfixes and stability improvements
- Rocky 9 packaging: split package layout and replace system libldb / ldb-tools to avoid file conflicts during install
- Fixed local state paths to use /var instead of /usr/var
- Package revision 4.23.6_01

* Thu Nov 20 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-9
- Adicionados pacotes depentendes na instalação no runtime, estavam quebrando a instalacao
- Ajustada unit systemd para Type=simple com ExecStart=/usr/sbin/samba -F
- Removida dependência de PIDFile e problemas de timeout no systemd

* Wed Nov 19 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-8
- Removidas todas duplicatas de BuildRequires
- Lista final segue DOC oficial do Samba + extras necessários

* Wed Nov 19 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-7
- Enxugados Requires para seguir a lista de libs do doc oficial do Samba
- Mantidos apenas Conflicts/Obsoletes/Provides para pacotes samba*, libwbclient
- Removidos Conflicts/Obsoletes/Provides sobre libldb/python3-ldb/python3-tdb (evita quebrar sssd)
- Mantidos serviço systemd samba-ad-dc.service e checagem de repositórios

* Wed Nov 19 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-6
- Mantido replacement completo da pilha Samba/libldb/python3 da distro
- Removidos Requires para libldb/python3-ldb (evita puxar pacotes da base e conflito com samba-client-libs)
- Mantidos Conflicts/Obsoletes/Provides para libldb, python3-ldb, python3-tdb, samba*, libwbclient
- Mantido serviço systemd samba-ad-dc.service e checagem de repositórios

* Wed Nov 19 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-5
- Adicionada unit systemd samba-ad-dc.service:
- ExecStart=/usr/sbin/samba -D, PIDFile=/run/samba/samba.pid
- Instalada em {_unitdir}
- Integrada com macros systemd_post/preun/postun_with_restart

* Wed Nov 19 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-4
- Ajustado para coexistir com sssd-common (libldb da base):
- Restaurados Requires para libldb/python3-ldb
- Removidos Conflicts/Obsoletes/Provides sobre libldb, ldb-tools, python3-ldb, python3-tdb
- Removidos módulos /usr/lib64/samba/ldb/*.so do pacote para evitar conflito com libldb da base

* Tue Nov 18 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-3
- Transformado o pacote samba em replacement completo do stack Samba/libldb da distro.
- Removidos Requires de libldb/python3-ldb da base.
- Adicionados Conflicts/Obsoletes/Provides para libldb, ldb-tools, python3-ldb, python3-tdb, samba*, libwbclient.
- Incluídas todas as libs/módulos em {_libdir}/samba/ no pacote principal.

* Mon Nov 17 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-2
- Split private Samba libraries into samba-private-libs subpackage
- Keep libldb-cmdline-private-samba.so to satisfy private LDB symbol
- Adjust BuildRequires for EL9/EL10 (libxslt, libtalloc/libtevent, drop python3-*-devel)
- Fix filelist to not own /usr/sbin (filesystem conflict)

* Sat Nov 15 2025 Guilherme Suzin <gui.suzin@live.com> - 4.23.3-1
- Initial packaging for EL9/EL10 (configure/make, manifest, smb.conf ghost)
