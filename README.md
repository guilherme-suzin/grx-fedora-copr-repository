# 🖧 Samba AD DC para RHEL 9.x e RHEL 10

**Repositório: `guilherme-suzin/grx-enterprise` (Samba 4.23.x / 4.24.x)**

Este repositório fornece versões corporativas atualizadas do **Samba AD DC** para todas as distribuições baseadas em:

* **RHEL 9.x / CentOS Stream 9 / Rocky 9.x / AlmaLinux 9.x**
* **RHEL 10 / CentOS Stream 10 / Rocky 10**

Mantido pela **Onbit Technology**.

---

## 📌 Sobre

Os pacotes são compilados seguindo as recomendações do **bootstrap oficial do Samba**, garantindo:

* Ambientes AD DC estáveis
* Compatibilidade 100% MIT Kerberos
* Dependências alinhadas ao upstream
* Instalação padronizada em `/usr`, `/etc/samba`, `/var/lib/samba`

---

# 🚀 Instruções de Instalação

Atenção:
O procedimento muda ligeiramente entre **RHEL 9** e **RHEL 10**.

---

# ▶️ **1. Pré-requisitos (válidos para RHEL 9 e RHEL 10)**

```bash
sudo dnf install -y dnf-plugins-core epel-release
sudo dnf config-manager --set-enabled crb
sudo dnf update -y
```

---

# ▶️ **2. Dependências específicas por versão**

---

## 🟩 **RHEL 9.x / Rocky 9.x / AlmaLinux 9.x**

O Samba upstream **exige GlusterFS 9 para build** no RHEL9.

Instale:

```bash
sudo dnf install -y centos-release-gluster9
```

E depois:

```bash
sudo dnf install -y glusterfs-api-devel glusterfs-devel
```

---

## 🟦 **RHEL 10 / Rocky 10**

❗ **IMPORTANTE:**
O RHEL 10 **não possui GlusterFS** nos repositórios e o Samba upstream no EL10 **não requer glusterfs-devel** para AD DC.

Portanto, **NÃO instale**:

* `centos-release-gluster9`
* `glusterfs-api-devel`
* `glusterfs-devel`

Se instalar, irá quebrar o ambiente.

---

# 🧰 3. Instalar dependências do Samba (bootstrap oficial)

Essas dependências funcionam **tanto no RHEL 9 quanto no RHEL 10**, com exceção dos pacotes Gluster listados acima.

```bash
sudo dnf install -y \
    --setopt=install_weak_deps=False \
    acl attr autoconf avahi-devel bind-utils binutils bison \
    cargo ccache chrpath clang-devel crypto-policies-scripts cups-devel \
    dbus-devel docbook-dtds docbook-style-xsl flex gawk gcc gdb git \
    glib2-devel glibc-common glibc-langpack-en \
    gnutls-devel gnutls-utils gpgme-devel gzip hostname \
    jansson-devel jq keyutils-libs-devel ldb-tools \
    krb5-devel krb5-server krb5-workstation \
    libacl-devel libarchive-devel libattr-devel libblkid-devel libbsd-devel \
    libcap-devel libevent-devel libicu-devel libpcap-devel \
    libtasn1-devel libtasn1-tools libtirpc-devel libunwind-devel \
    liburing-devel libuuid-devel libxslt lmdb lmdb-devel \
    lsb_release make mingw64-gcc ncurses-devel \
    openldap-devel openssl-devel pam-devel patch perl \
    perl-Archive-Tar perl-ExtUtils-MakeMaker perl-Parse-Yapp perl-Test-Simple \
    perl-generators perl-interpreter pkgconfig popt-devel \
    procps-ng psmisc python3 python3-cryptography python3-devel \
    python3-dns python3-gpg python3-iso8601 python3-libsemanage \
    python3-markdown python3-policycoreutils python3-pyasn1 \
    python3-requests python3-setproctitle \
    quota-devel readline-devel rng-tools rpcgen \
    rpcsvc-proto-devel rsync sed sudo systemd-devel \
    tar tracker-devel tree utf8proc-devel wget which \
    xfsprogs-devel xz yum-utils zlib-devel
```

📌 **Nota:**
No RHEL10, simplesmente ignore os pacotes Gluster listados no bloco acima (eles não existem e não são mais necessários).

---

# 🟪 4. Instalar Samba do repositório Onbit

```bash
sudo dnf copr enable guilherme-suzin/grx-enterprise -y
sudo dnf install samba -y
```

---

#  Possíveis Erros
Necessidade de remover o sssd-common;
Necessidade de remover python3-tevent;
Necessidade de remover samba* (antes de instalar o samba do repositório da GRX);

```bash
sudo dnf remove sssd-common python3-tevent
```

---

# 📁 Estrutura instalada

* `/usr/bin`
* `/usr/sbin`
* `/etc/samba`
* `/var/lib/samba`
* `/usr/lib64/samba` (libs privadas)

---

# 👤 Maintainer

**GRX Solutions — Soluções Tecnológicas Inovadoras para seu Negócio**
🌐 [https://grxsolutions.co](https://grxsolutions.co)
📧 [gui.suzin@live.com](mailto:gui.suzin@live.com)
