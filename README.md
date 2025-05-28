## 🇬🇧 English Version

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
   `https://github.com/vagvom/lsc_camera`
3. Install the integration and restart Home Assistant

### Manual Installation

1. Clone or download this repository
2. Copy the `lsc_camera` folder into `custom_components/`
3. Restart Home Assistant

---

## Configuration

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=vagvom&repository=lsc_camera_ha&category=integration)

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

## License and Usage

This project is distributed under the **GNU GPLv3** license, which means the code is free and open source. You may copy, modify, and redistribute it as long as you comply with the license terms.

**Warning:** Any commercial use of this code (selling, integrating into a paid product, etc.) requires prior agreement with the author (`vagvom`).

The goal is to keep the project free while protecting the work from unauthorized commercial exploitation.

---





---

## 🇫🇷 Version Française

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

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=vagvom&repository=lsc_camera_ha&category=integration)

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
Voici un petit paragraphe que tu peux ajouter dans ton README, par exemple dans une section **Licence** ou **À propos** :

---

## Licence et utilisation

Ce projet est distribué sous licence **GNU GPLv3**, ce qui signifie que le code est libre et ouvert. Vous pouvez le copier, le modifier et le redistribuer tant que vous respectez les termes de la licence.

**Attention :** toute utilisation commerciale de ce code (vente, intégration dans un produit payant, etc.) doit faire l'objet d'un accord préalable avec l'auteur (`vagvom`).

L’objectif est de garantir que le projet reste libre tout en protégeant le travail réalisé contre une exploitation commerciale non autorisée.

---

