## 🖧 Samba AD DC — GRX Solutions

Repositório: `guilherme-suzin/grx-enterprise`

Este repositório fornece versões corporativas do **Samba AD DC** prontas para uso em:

- RHEL 9.x / Rocky Linux 9 / AlmaLinux 9 / CentOS Stream 9  
- RHEL 10 / Rocky Linux 10 / CentOS Stream 10  

---

# 🚀 Instalação

## ⚠️ Etapa 1 — Limpeza do ambiente (OBRIGATÓRIO)

Antes de instalar o Samba da GRX, remova qualquer instalação anterior e limpe o ambiente.

```bash
sudo systemctl stop samba smb nmb winbind 2>/dev/null || true

sudo dnf remove -y sssd-common python3-tevent samba*

# Remove base antiga do domínio
sudo rm -rf /var/lib/samba

# Backup opcional do smb.conf
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak.$(date +%F-%H%M%S) 2>/dev/null || true
````

---

## ▶️ Etapa 2 — Habilitar repositório GRX

```bash
sudo dnf install -y dnf-plugins-core epel-release
sudo dnf config-manager --set-enabled crb

sudo dnf copr enable guilherme-suzin/grx-enterprise -y
```

---

## ▶️ Etapa 3 — Instalar Samba

```bash
sudo dnf install samba -y
```

---

# 📌 Observações importantes

* O pacote da GRX resolve automaticamente todas as dependências
* Não é necessário instalar pacotes manualmente
* Pronto para uso como **Active Directory Domain Controller (AD DC)**
* Recomendado uso em ambiente limpo (sem resíduos de instalações anteriores)

---

# 📁 Estrutura instalada

* `/usr/bin`
* `/usr/sbin`
* `/etc/samba`
* `/var/lib/samba`
* `/usr/lib64/samba`

---

# 🔧 Pós-instalação (exemplo básico)

## Provisionar domínio

```bash
samba-tool domain provision \
  --use-rfc2307 \
  --realm=SUZIN.LOCAL \
  --domain=SUZIN \
  --server-role=dc
```

## Iniciar serviço

```bash
systemctl enable samba-ad-dc --now
```

---

# ⚠️ Boas práticas

* Configure corretamente o DNS antes de ingressar máquinas no domínio
* Garanta sincronização de horário (NTP) entre clientes e servidor
* Utilize firewall liberando portas necessárias do Samba AD
* Não misturar com SSSD em modo AD no mesmo host

---

# 👤 Maintainer

**GRX Solutions — Soluções Tecnológicas Inovadoras para seu Negócio**
🌐 [https://grxsolutions.co](https://grxsolutions.co)
📧 [gui.suzin@live.com](mailto:gui.suzin@live.com)

