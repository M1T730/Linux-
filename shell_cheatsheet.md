# Shell Cheatsheet


```bash
#!bin/bash
variabili = 
$"variabile"
$(comando)
$((variabile1 + variabile2))
export MY_VARIABLE="Hello from my variable"
$0                          # script name
$1,2...                     # arguments
if [ $# - eq]; then               # if /numero di arguments /equals
elseif else fi 
for arg in "$@"; do             # for loop
done
array=()
array+=(1,"hello")
${array[0]}                     #array as variable
NumberOfNames=${#NAMES[@]}      # list number of elemets 
```