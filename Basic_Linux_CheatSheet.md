# Cheatsheet

## 1. Informazioni sul sistema e utente
```bash
whoami
id
id -un
echo ~
```

## 2. Navigazione nel filesystem
```bash

pwd
ls
ls ~
ls -r
ls -a
ls -R
ls -l
cd nome_directory
cd ..
cd ~
cd -
cd .
```

## 3. Creazione e gestione file
```bash
touch nome_file
touch -r nome_file1 nome_file2
touch -d "2026-02-13 00:42" nome_file
cat nome_file
cat -n                              # numeri tutte le righe
cat -b                              # numeri righe non vuote
cat > 
echo "" > file.txt
.hidden_file
```

## 4. Creazione e gestione directory
```bash
mkdir nome_directory
rmdir nome_directory
rm -r nome_directory
```

## 5. Copia file e directory
```bash
cp nome_file nome_copia
cp -r directory copy_directory
```
## 6. Spostamento e rinomina
```bash
mv file_name.txt new_name.txt
mv file.txt directory_name
mv directory_name new_directory
```

## 7. Rimozione file
```bash
rm file.txt
rm -i file.txt
rm -f file.txt
rm -rf directory_name
```

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
history -d      # elimina voce
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

```bash
sudo
chown owner:group
chown -r owner:group
chmod 0-7(r=4,w=2,x=1)    # permessi numerici
chmod (u/g/o)(+/-)(r/w/x) # permessi simbolic 
ls -d 
sudo useradd 
sudo useradd -m           # crea user con home
sudo passwd 
sudo passwd -l            # lock
sudo passwd -u            # unlock
grep
grep -w                   # whole(\b\b)
greg -i                   # ignora case
greg -v                   # non contiene...
grep -n                   # numero riga
greg -r/-R                # directory
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



```