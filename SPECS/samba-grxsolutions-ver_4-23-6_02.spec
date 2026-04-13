Name:           samba
Version:        4.23.6
Release:        2%{?dist}
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

# ==== BuildRequires unificado (ordenado alfabeticamente) ===================

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

# ==== Snapper opcional =====================================================
%if %{with snapper}
BuildRequires:  dbus
BuildRequires:  dbus-devel
%endif

# ==== Selftest opcional ====================================================
%if %{with check}
BuildRequires:  bash
BuildRequires:  python3-iso8601
BuildRequires:  python3-cryptography
BuildRequires:  python3-pyasn1
%endif

# ==== Runtime Requires (seguindo DOC OFICIAL Samba) ========================
Requires: acl
Requires: attr
Requires: cups
Requires: dbus-libs
Requires: flex
Requires: gnutls >= 3.4.7
Requires: gpgme
Requires: jansson
Requires: krb5-libs
Requires: krb5-workstation
Requires: libacl
Requires: libaio
Requires: libarchive
Requires: libattr
Requires: libblkid
Requires: libbsd
Requires: libtasn1
Requires: libtasn1-tools
Requires: libxml2
Requires: libxslt
Requires: lmdb
Requires: openldap
Requires: pam
Requires: patch
Requires: perl
Requires: perl-ExtUtils-MakeMaker
Requires: perl-Parse-Yapp
Requires: popt
Requires: python3
Requires: python3-cryptography
Requires: python3-dns
Requires: python3-gpg
Requires: python3-iso8601
Requires: python3-libsemanage
Requires: python3-markdown
Requires: python3-policycoreutils
Requires: python3-pyasn1
Requires: python3-requests
Requires: python3-setproctitle
Requires: readline
Requires: rpcgen
Requires: systemd
Requires: tar
Requires: zlib

# ==== Replacement somente dos pacotes Samba ================================
Conflicts: samba
Conflicts: samba-common
Conflicts: samba-common-libs
Conflicts: samba-client-libs
Conflicts: libwbclient

Obsoletes: samba < %{version}
Obsoletes: samba-common < %{version}
Obsoletes: samba-common-libs < %{version}
Obsoletes: samba-client-libs < %{version}
Obsoletes: libwbclient < %{version}

Provides: samba-common = %{version}-%{release}
Provides: samba-common-libs = %{version}-%{release}
Provides: samba-client-libs = %{version}-%{release}
Provides: libwbclient = %{version}-%{release}

# ==== Scriptlets systemd ===================================================
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Samba provides SMB/CIFS file and print services and can act as an Active Directory
domain controller. Several utilities (e.g. samba-tool) and the build system are
written in Python 3.x.

%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=/usr \
   --exec-prefix=/usr \
   --libdir=%{_libdir} \
   --sbindir=%{_sbindir} \
   --sysconfdir=/etc \
   --localstatedir=/var \
   --mandir=/usr/share/man \
   --enable-fhs \
   --bundled-libraries=cmocka

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Corrige conflito com brp-compress/manpages
rm -rf %{buildroot}%{_mandir}/man1 || true
rm -rf %{buildroot}%{_mandir}/man3 || true
rm -rf %{buildroot}%{_mandir}/man5 || true
rm -rf %{buildroot}%{_mandir}/man7 || true
rm -rf %{buildroot}%{_mandir}/man8 || true

# NÃO REMOVER libs privadas do Samba / LDB, pois são necessárias.
# Apenas remover manpage de talloc (conflito com libtalloc-devel do sistema)
rm -f %{buildroot}%{_mandir}/man3/talloc.3* || true

# NÃO remova os bindings Python aqui, porque eles fazem parte da pilha
# que você está fornecendo (python3-ldb, python3-tdb etc).

# Instala unidade systemd para AD DC
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

# Manifesto: arquivos do pacote principal
find %{buildroot} -mindepth 1 \( -type f -o -type l -o -type d \) \
   | sed "s|^%{buildroot}||" \
   | grep -vE '^/$|^%{_sbindir}$|^/usr$|^/usr/bin$|^/usr/lib$|^/usr/lib64$' \
   | grep -vE '^/usr/lib/debug/|^/usr/lib/.build-id/|^%{_mandir}/' \
   | sort -u > %{_builddir}/filelist.manifest

%post
# Ativa/atualiza serviço systemd
%systemd_post samba-ad-dc.service

# Cria um smb.conf básico na primeira instalação (não sobrescreve)
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

%preun
%systemd_preun samba-ad-dc.service

%postun
%systemd_postun_with_restart samba-ad-dc.service

%check
%if %{with check}
# Selftests desabilitados por padrão; habilite com --with check
true
%endif

# ====================================================================
# Pacote principal
# ====================================================================

%files -f %{_builddir}/filelist.manifest
%license COPYING
%doc README*
%dir %{_sysconfdir}/samba
%config(noreplace) %ghost %{_sysconfdir}/samba/smb.conf
%{_unitdir}/samba-ad-dc.service

%changelog
* Sun Apr 12 2026 Guilherme Suzin <gui.suzin@live.com> - 4.23.6-2
- Retry build for new GRX COPR repository
- Keep legacy single-package layout for compatibility with previous successful COPR workflow
- Keep manual manpage cleanup during %%install to avoid brp-compress conflicts
- Preserve Samba AD DC systemd unit and default smb.conf bootstrap
- Rebuild package for validation in clean COPR chroot

* Sat Mar 07 2026 Guilherme Suzin <suporte@onbit.tech> - 4.23.6-1
- Update to Samba 4.23.6
- Keep single-package layout compatible with existing COPR workflow
- Added --localstatedir=/var to fix /usr/var/lib/samba path issue
- Fixed ghost path for /etc/samba/smb.conf
- Use parallel make with %%{?_smp_mflags}
- Removed installed manpages during %%install to avoid brp-compress manifest conflicts
- Package revision 4.23.6_03

* Thu Nov 20 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-9
- Adicionados pacotes depentendes na instalação no runtime, estavam quebrando a instalacao
- Ajustada unit systemd para Type=simple com ExecStart=/usr/sbin/samba -F
- Removida dependência de PIDFile e problemas de timeout no systemd

* Wed Nov 19 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-8
- Removidas todas duplicatas de BuildRequires
- Lista final segue DOC oficial do Samba + extras necessários

* Wed Nov 19 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-7
- Enxugados Requires para seguir a lista de libs do doc oficial do Samba
- Mantidos apenas Conflicts/Obsoletes/Provides para pacotes samba*, libwbclient
- Removidos Conflicts/Obsoletes/Provides sobre libldb/python3-ldb/python3-tdb (evita quebrar sssd)
- Mantidos serviço systemd samba-ad-dc.service e checagem de repositórios

* Wed Nov 19 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-6
- Mantido replacement completo da pilha Samba/libldb/python3 da distro
- Removidos Requires para libldb/python3-ldb (evita puxar pacotes da base e conflito com samba-client-libs)
- Mantidos Conflicts/Obsoletes/Provides para libldb, python3-ldb, python3-tdb, samba*, libwbclient
- Mantido serviço systemd samba-ad-dc.service e checagem de repositórios

* Wed Nov 19 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-5
- Adicionada unit systemd samba-ad-dc.service:
- ExecStart=/usr/sbin/samba -D, PIDFile=/run/samba/samba.pid
- Instalada em {_unitdir}
- Integrada com macros systemd_post/preun/postun_with_restart

* Wed Nov 19 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-4
- Ajustado para coexistir com sssd-common (libldb da base):
- Restaurados Requires para libldb/python3-ldb
- Removidos Conflicts/Obsoletes/Provides sobre libldb, ldb-tools, python3-ldb, python3-tdb
- Removidos módulos /usr/lib64/samba/ldb/*.so do pacote para evitar conflito com libldb da base

* Tue Nov 18 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-3
- Transformado o pacote samba em replacement completo do stack Samba/libldb da distro.
- Removidos Requires de libldb/python3-ldb da base.
- Adicionados Conflicts/Obsoletes/Provides para libldb, ldb-tools, python3-ldb, python3-tdb, samba*, libwbclient.
- Incluídas todas as libs/módulos em {_libdir}/samba/ no pacote principal.

* Mon Nov 17 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-2
- Split private Samba libraries into samba-private-libs subpackage
- Keep libldb-cmdline-private-samba.so to satisfy private LDB symbol
- Adjust BuildRequires for EL9/EL10 (libxslt, libtalloc/libtevent, drop python3-*-devel)
- Fix filelist to not own /usr/sbin (filesystem conflict)

* Sat Nov 15 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-1
- Initial packaging for EL9/EL10 (configure/make, manifest, smb.conf ghost)
