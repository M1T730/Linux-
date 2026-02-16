# Cheatsheet


d1: 

```bash
whoami
id
id -un
echo ~
pwd
ls
ls ~
ls -r
ls -a
ls -R
ls -l                       # -(type) ---(ownerperms)---(groupperms)---(otherperms) n(hardlinks) owner group N(bites) data(orario) file
cd nome_directory
cd ..
cd ~
cd -
cd .
touch nome_file.txt
touch -r file1.txt file2.txt        # syncronizza timestamp
touch -d "2026-02-13 00:42" nome_file.txt   # set timestamp
cat nome_file.txt
cat -n                              # numeri tutte le righe
cat -b                              # numeri righe non vuote
cat > nome_file.txt                  # scrive da stdin
echo "" > file.txt                   # svuota il file.txt
.hidden_file
mkdir nome_directory
rmdir nome_directory
rmdir -r nome_directory
cp nome_file.txt copia.txt
cp -r directory copy_directory
mv file_name.txt new_name.txt
mv file.txt directory_name
mv directory_name new_directory
rm file.txt
rm -i file.txt                       # chiedi conferma
rm -f file.txt                       # forza cancellazione
rm -rf directory_name                 # cancella ricorsivamente
```

d2:

```bash
head 
head -n
tail
tail -n
diff 
diff -r
file 
less file.txt
!!
control-r
history
history -c      # cancella cronologia
history -w      # salva cronologia
history -d    # elimina voce
clear
ls/cp *.txt     # wildcard multipla
ls/cp file?.txt # un carattere
ls/cp file[].txt # set caratteri
-i flag 
cp -p           # preserva attributi
mv -t /somedirectory file_1 file_2
mv -v           # verbose
mv -b           # backup
mkdir -p test/test1/test2/test3/test4
find [path] [expression]
find -type 
find -name 
find -maxdepth (subdic)
find -empty
find -mtime +/- (giorni)
find -ipath 
find -user
find -group 
find -size 
help
--help
alias name='command'
nano ~/.bashrc (permanent alias)
source ~/.bashrc (reload config)
unalias
exit 
logout
```

d3:

```bash
sudo
chown owner:group
chown -r owner:group
chmod 0-7(r=4,w=2,x=1)    # permessi numerici
chmod (u/g/o)(+/-)(r/w/x) # permessi simbolic 
ls -d                      # list dir
sudo useradd 
sudo useradd -m           # crea user con home
sudo grep -w '' /etc/passwd     # username/password(nascostoIn/etc/shadow)/UID/GID/homedir/shell
sudo passwd 
sudo passwd -l            # lock
sudo passwd -u            # unlock
grep
grep -e  # for all the options( -v, -w, -i) explicit next argument is pattern
grep -w                   # whole(\b\b)
grep -i                   # ignora case
grep -v                   # non contiene...
grep -n                   # numero riga
grep -r/-R                # directory
grep -c                   # count 
grep -o                   # solo
grep -f patterns.txt sample.txt # multiple patters 
sudo usermod 
sudo usermod -d /home
sudo usermod -s /bin/bash
sudo usermod -G           # sovrascrivere gruppo
sudo usermod -aG          # aggiungere a gruppo
sudo usermod -md          # directory muovendo file
sudo usermod -l           # camb nome
sudo usermod -u           # camb UID
sudo usermod -L           # lock
sudo usermod -U           # unlock 
groups                    # list groups of user
su - username             # switch user
sudo userdel -r 
echo >
echo >>
cat >
cat < >
2>/dev/null                 # molto comodo per cestinare errs
|
| tee 
env                       # enviroment parameters
export env = 
nano ~/.bashrc (permanent env)
source ~/.bashrc (reload config)
cut -c                      # char
cut -f                      # tab
cut -fd " "                 # spazio al posto di tab
paste -s                   
paste -s -d " "             # repara per spazio(tab default)
tail -f                     # continuo
expand 
expand -t n                  # da tab a n spazio(default 8)
unexpand
unexpand -t n                # da n spazio a tab(default 8)
join
join -n                      # decidere dove la linee "va"
split
split -b                     # split per spazio byte(K,M,G)
split -l n                   # split per linee (default 1000)
sort 
sort -r                     # reverse
sort -n                     # by number
tr a-z A-Z                  # togliere lowercase
tr -d                       # eliminare 
tr -s                       # tutto 1 spazio solo
uniq                        # solo direttamente adiacenti
uniq -c                     # conta il numero
uniq -u                     # solo non ripetute
uniq -d                     # solo ripetute
wc                          # linee/parole/bytes
wc -l/-w/-c
nl                          # numera linee
```
https://overthewire.org/wargames/bandit/bandit10.html
bandit level 9 ora, passwd: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

d4:

```bash
sudo passwd -S              # username/status/data/mindays/maxdays/expireddays/accdisactivetionday
grep -E '^(joker|batman):'  # più oggetti 
uname                       # nome sistema
uname -a                    # kernel/hostname/versione/buildN/multicoresupport/data/compilazione/cpuArch/kernelArch/SO
uptime                      # oracorrente/tempodiattività/utentiloggati/loadaverage
top (fondamentale)          # processi attivi in tempo reale principali: PID/user/memoria/cpu/tempo/comando
ls -F                       # aggiungere carattere speciale in base al file: (dic(/),sh(*),socker(=))
tar -czf archive.tar.gz file1 file1 # create new archive/compress archive using gzip/specify filename
who             # username/terminale/logintime/ip spesso usato spesso insieme a uptime, chi è loggato?
w               # uptime/username/terminale/ip/orariologin/idle/cpuSessione/cpuProcesso/cosa sta facendo?(bash/top ecc..) 
regex: . * + ? [] [^] () ‘ ^ $
```

bandit level 13 ora, passwd: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

d5:
```bash
tar -xf                    # decompress
gunzip
bunzip
sudo chmod -g+s / 2xxx       #set group id(SGID)
sudo chmod -u+s / 4xxx       #set user id(SUID)
sudo chmod +t / 1xxx  dir      #set sticky bit
dmesg                       # view kernel messages
visudo                      # best practice to change /etc/sudoers
sudo chgrp                  # cambiare  gruppo di un file
sudo chown user:group 
umask                       # temporaneamente cambiare permessi dei prossimi file creati (funziona al crontrario di chmod)
ps                          # PID/TTY/STAT/TIME/CMD
ps a u x                    # all processes for all users/ detailes/ processes not attached to terminal(daemons)
ps -ef                      # every process on system , full format: (UID,PID,PPID,C,STIME)
```bash