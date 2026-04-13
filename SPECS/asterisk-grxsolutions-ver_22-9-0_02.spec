Name:           asterisk
Version:        22.9.0
Release:        2%{?dist}
Summary:        Asterisk Open Source PBX com Suporte Completo (PJSIP, SNMP)

License:        GPLv2
URL:            https://www.asterisk.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        pjproject-2.16.tar.bz2
Source2:        jansson-2.14.1.tar.bz2

# ====================================================================
# BuildRequires (Final - Otimizado para EPEL Build)
# ====================================================================

# Build system básico
BuildRequires:  make gcc gcc-c++ pkgconfig autoconf-archive

# Asterisk: requisitos básicos
BuildRequires:  libedit-devel libuuid-devel sqlite-devel libxml2-devel

# Asterisk: para addons e features (Pacotes não essenciais/problemáticos removidos)
BuildRequires:  speex-devel speexdsp-devel libogg-devel libvorbis-devel portaudio-devel libcurl-devel xmlstarlet bison flex
BuildRequires:  postgresql-devel unixODBC-devel neon-devel lua-devel uriparser-devel libxslt-devel openssl-devel
BuildRequires:  mariadb-devel bluez-libs-devel radcli-devel freetds-devel bash libcap-devel
BuildRequires:  net-snmp-devel newt-devel popt-devel libical-devel spandsp-devel
BuildRequires:  binutils-devel libsrtp-devel gsm-devel doxygen graphviz zlib-devel openldap-devel
BuildRequires:  codec2-devel fftw-devel libsndfile-devel unbound-devel

# Para PJProject e MP3 Source
BuildRequires:  wget subversion bzip2 patch

# Requisitos básicos em tempo de execução
Requires:       ncurses
Requires:       openssl
Requires:       sqlite
Requires:       libxml2
Requires:       jansson
Requires:       libuuid
Requires:       libcurl

%description
Asterisk é um framework open source para a construção de aplicações de comunicações. 
Este pacote foi configurado para incluir suporte a: PJSIP (SIP moderno), formato MP3, 
SNMP, e diversas outras funcionalidades, sendo compatível com os ambientes EPEL 9 e EPEL 10.

# ====================================================================
# prep
# ====================================================================
%prep
%autosetup -n %{name}-%{version}

# ====================================================================
# build: Comandos detalhados para compilação completa e Sons (en-us)
# ====================================================================
%build
# 1. Configura o Asterisk
# Prepara bundled offline para evitar downloads externos no COPR
mkdir -p third-party/pjproject/source
mkdir -p third-party/jansson/source

cp -f %{SOURCE1} third-party/pjproject/source/pjproject-2.16.tar.bz2
cp -f %{SOURCE2} third-party/jansson/source/jansson-2.14.1.tar.bz2

# Usa /usr/lib64 para garantir o FHS (Filesystem Hierarchy Standard) do RHEL/EPEL.
./configure \
    --prefix=/usr \
    --libdir=/usr/lib64 \
    --sysconfdir=%{_sysconfdir} \
    --with-pjproject-bundled \
    --with-jansson-bundled

# 2. Configura Módulos via menuselect (non-interativo)
make menuselect.makeopts

# 3. Habilita módulos e sons (CORE e EXTRA, uLaw e WAV)
menuselect/menuselect \
    --enable app_stack \
    --enable res_snmp \
    --enable CORE-SOUNDS-EN_US-ULAW \
    --enable CORE-SOUNDS-EN_US-WAV \
    --enable EXTRA-SOUNDS-EN_US-ULAW \
    --enable EXTRA-SOUNDS-EN_US-WAV \
    menuselect.makeopts

# 4. Compilação Paralela
make %{?_smp_mflags} all

# ====================================================================
# install: Instalação e Organização dos Arquivos
# ====================================================================
%install
# Criação de diretórios
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/asterisk
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk

# Instala binários, bibliotecas e módulos
make install DESTDIR=%{buildroot}

# Instala arquivos de configuração de exemplo (samples)
make samples DESTDIR=%{buildroot}

# Instala scripts de inicialização (config)
make config DESTDIR=%{buildroot}

# Instalação dos Áudios Padrão (EN-US)
make core-sounds-en-us-ulaw install DESTDIR=%{buildroot}
make core-sounds-en-us-wav install DESTDIR=%{buildroot}
make extra-sounds-en-us-ulaw install DESTDIR=%{buildroot}
make extra-sounds-en-us-wav install DESTDIR=%{buildroot}

# ====================================================================
# files: Lista de Arquivos
# ====================================================================
%files
%doc doc/*
%license COPYING

# Binários, libs, módulos e arquivos de configuração
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*
%{_libdir}/asterisk/*
%config(noreplace) %{_sysconfdir}/asterisk/*

# Diretórios de estado e spool
%dir %{_localstatedir}/spool/asterisk

# Diretórios de Áudio (no /var/lib/asterisk/sounds)
%dir %{_localstatedir}/lib/asterisk
%dir %{_localstatedir}/lib/asterisk/sounds
%{_localstatedir}/lib/asterisk/sounds/en_US/*

# ====================================================================
# changelog
# ====================================================================
%changelog
* Sun Apr 12 2026 Guilherme Suzin <gui.suzin@live.com> - 22.9.0-2
- Use bundled PJProject and bundled Jansson with local sources for offline COPR build
- Remove duplicate prep macro usage
- Preserve PJSIP, SNMP and default sound packages
- Adjust package metadata to current enabled feature set

* Sun Apr 12 2026 Guilherme Suzin <gui.suzin@live.com> - 22.9.0-1
- Update to Asterisk 22.9.0
- Upgrade from 22.6.0 to latest stable 22.x release
- Updated bundled PJProject (2.16) for improved SIP/WebRTC handling
- Improved PJSIP stability and performance
- Enhancements in CDR/CEL processing performance
- Improvements in ARI and HTTP subsystem (ACL and security controls)
- Fixes in DTLS, TURN and WebRTC media handling
- Improvements in app_queue behavior and reliability
- Enhancements in chan_websocket for real-time communication use cases
- General bug fixes and performance improvements across SIP, media and core modules
- Maintained GRX packaging model with bundled dependencies and full feature set (MP3, PJSIP, SNMP, sounds)

* Tue Nov 18 2025 Guilherme Suzin <suporte@onbit.tech> - 22.6.0-1
- Criação do pacote RPM para o Asterisk 22.6.0, compatível com EPEL 9/10. Corrigidas 
  dependências BuildRequires para nomes de pacotes do RHEL 9/10 e incluídos sons padrão.
