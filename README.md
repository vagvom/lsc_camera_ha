# Intégration LSC Camera pour Home Assistant

Bonjour, voici mon projet.  
Le but est d’intégrer les caméras de la marque LSC (trouvées chez Action), rootées via le projet de @guino [LSCOutdoor1080P](https://github.com/guino/LSCOutdoor1080P), directement dans Home Assistant.  

Le projet est assez simple et manque d’améliorations, c’est mon premier projet d’intégration Home Assistant et je ne connais pas du tout Python.  
N’hésitez pas à me faire part de vos idées pour l’améliorer !

---

## Description

Cette intégration personnalisée permet d’ajouter et de contrôler les caméras IP rootées de la marque LSC dans Home Assistant.  
Elle supporte le streaming vidéo via RTSP, le contrôle des mouvements de la caméra (haut, bas, gauche, droite),  
la synchronisation de l’heure via Telnet, ainsi que l’activation/désactivation de Telnet via HTTP.

---

## Fonctionnalités principales

- **Streaming vidéo en direct**  
  Visualisez le flux vidéo principal via RTSP avec prise en charge FFmpeg.

- **Contrôle de la caméra** (uniquement sur caméras 360°)  
  Boutons pour déplacer la caméra vers le haut, bas, gauche et droite.

- **Synchronisation de l’heure**  
  Bouton pour synchroniser l’heure de la caméra avec celle du serveur Home Assistant via Telnet.

- **Activation/désactivation de Telnet**  
  Commandes HTTP pour activer ou désactiver Telnet sur la caméra.

---

## Prérequis

- Home Assistant version 2024.1.0 ou ultérieure  
- Accès réseau à la caméra LSC (IP, utilisateur, mot de passe)  
- Port Telnet (par défaut 24) ouvert si vous utilisez la synchronisation de l’heure ou le toggle Telnet

---

## Installation

### Via HACS (recommandée)

1. Ouvrez **HACS** → **Intégrations** → cliquez sur **+**  
2. Choisissez **Dépôt personnalisé**  
3. Entrez l’URL du dépôt :  
   `https://github.com/yourusername/lsc_camera`  
4. Sélectionnez **Intégration** comme type et validez  
5. Installez l’intégration depuis HACS  
6. Redémarrez Home Assistant

### Installation manuelle

1. Clonez ou téléchargez ce dépôt GitHub  
2. Copiez le dossier `lsc_camera` dans `custom_components` de Home Assistant  
3. Redémarrez Home Assistant

---

## Configuration

### Ajout via l’interface utilisateur

1. Allez dans **Paramètres** → **Appareils et services** → cliquez sur **Ajouter une intégration**  
2. Recherchez **LSC Camera**  
3. Entrez :  
   - **Adresse IP** : IP locale de la caméra  
   - **Nom d’utilisateur**  
   - **Mot de passe**  
   - **Nom de l’appareil** (optionnel)  
   - **Caméra 360°** : cochez si la caméra supporte les commandes de mouvement  
4. Validez, l’intégration est créée, les entités caméra et boutons apparaissent.

### Exemple YAML (pour utilisateurs avancés)

```yaml
lsc_camera:
  ip_address: 192.168.1.50
  username: admin
  password: votre_mdp
  device_name: Caméra Salon
  is_360: true
