## 🇬🇧 English Version

[![hacs\_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/tonpseudo/lsc_camera.svg)](https://github.com/tonpseudo/lsc_camera/releases/)
[![HA integration usage](https://img.shields.io/badge/dynamic/json?color=41BDF5\&logo=home-assistant\&label=integration%20usage\&suffix=%20installs\&cacheSeconds=15600\&url=https://analytics.home-assistant.io/custom_integrations.json\&query=\$.lsc_camera.total)](https://analytics.home-assistant.io/custom_integrations.json)

# Home Assistant - LSC Camera Integration

Custom integration to connect LSC (Action brand) IP cameras to Home Assistant, based on [LSCOutdoor1080P by @guino](https://github.com/guino/LSCOutdoor1080P).

---

## Key Features

* Live RTSP video stream via FFmpeg
* PTZ control (up/down/left/right) for 360° cameras
* Time synchronization via Telnet
* Telnet toggle via HTTP requests

---

## Requirements

* Home Assistant version 2024.1.0 or higher
* Network access to the LSC camera (IP, username, password)
* Telnet port (default 24) open for sync and Telnet toggle

---

## Installation

### Via HACS (recommended)

1. Open **HACS** → **Integrations** → click **+**
2. Add this custom repository:
   `https://github.com/tonpseudo/lsc_camera`
3. Install the integration and restart Home Assistant

### Manual Installation

1. Clone or download this repository
2. Copy the `lsc_camera` folder into `custom_components/`
3. Restart Home Assistant

---

## Configuration

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=lsc_camera)

### UI Setup

1. Go to **Settings** → **Devices & Services** → **Add Integration**
2. Search for **LSC Camera**
3. Enter IP, login, password, name, and enable 360° if needed
4. Confirm to complete setup

### YAML (advanced)

```yaml
lsc_camera:
  ip_address: 192.168.1.50
  username: admin
  password: your_password
  device_name: Living Room Camera
  is_360: true
```

---

## 🇫🇷 Version Française

[![hacs\_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/tonpseudo/lsc_camera.svg)](https://github.com/tonpseudo/lsc_camera/releases/)
[![HA integration usage](https://img.shields.io/badge/dynamic/json?color=41BDF5\&logo=home-assistant\&label=integration%20usage\&suffix=%20installs\&cacheSeconds=15600\&url=https://analytics.home-assistant.io/custom_integrations.json\&query=\$.lsc_camera.total)](https://analytics.home-assistant.io/custom_integrations.json)

# Home Assistant - Intégration Caméra LSC

Intégration personnalisée pour intégrer les caméras IP LSC (marque Action) dans Home Assistant, basée sur le projet [LSCOutdoor1080P de @guino](https://github.com/guino/LSCOutdoor1080P).

---

## Fonctionnalités principales

* Streaming vidéo en direct via RTSP avec FFmpeg
* Contrôle PTZ (haut, bas, gauche, droite) pour caméras 360°
* Synchronisation de l’heure via Telnet
* Activation/désactivation de Telnet via HTTP

---

## Prérequis

* Home Assistant version 2024.1.0 ou supérieure
* Accès réseau à la caméra LSC (IP, utilisateur, mot de passe)
* Port Telnet (par défaut 24) ouvert pour synchronisation heure ou toggle Telnet

---

## Installation

### Via HACS (recommandée)

1. Ouvrir **HACS** → **Intégrations** → cliquer sur **+**
2. Ajouter un dépôt personnalisé avec l’URL :
   `https://github.com/tonpseudo/lsc_camera`
3. Installer l’intégration et redémarrer Home Assistant

### Installation manuelle

1. Cloner ou télécharger ce dépôt
2. Copier le dossier `lsc_camera` dans `custom_components/`
3. Redémarrer Home Assistant

---

## Configuration

[![Ouvrez votre instance Home Assistant et commencez la configuration d'une nouvelle intégration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=lsc_camera)

### Interface utilisateur

1. Aller dans **Paramètres** → **Appareils et services** → **Ajouter une intégration**
2. Chercher **LSC Camera**
3. Saisir IP, login, mot de passe, nom, et activer caméra 360° si besoin
4. Valider, l’intégration s’ajoute avec les entités

### YAML (option avancée)

```yaml
lsc_camera:
  ip_address: 192.168.1.50
  username: admin
  password: votre_mdp
  device_name: Caméra Salon
  is_360: true
```
