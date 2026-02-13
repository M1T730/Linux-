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
cat -n
cat -b
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
history -c
history -w
history -d
clear
ls/cp *.txt
ls/cp file?.txt
ls/cp file[].txt
-i flag 
cp -p 
mv -t /somedirectory file_1 file_2
mv -v
mv -b
mkdir -p test/test1/test2/test3/test4
file [path] [expression]
file -type 
file -name 
file -maxdepth
file -empty
file -mtime +/-
file -ipath 
help
--help
alias name='command'
nano ~/.bashrc (permanent alias)
source ~/.bashrc (reload config)
unalias
exit 
logout
```

