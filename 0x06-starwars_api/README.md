<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x06. Star Wars API 

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x) 
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should be `semistandard` compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All files must be executable
- The length of files will be tested using `wc`
- Not allowed to use `var`

## Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

## Install semi-standard
[Documentation](https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw)
```
$ sudo npm install semistandard --global

```
## Install request module and use it
[Documentation](https://intranet.alxswe.com/rltoken/BWz2gc45S-nZaxEY6GA6Zw)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
## Tasks
### 0. Star Wars Characters
Write a script that prints all characters of a Star Wars movie:

  - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
  - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
  - You must use the [Star wars API](https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg)
  - You must use the request module

```
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 
```
</div>
