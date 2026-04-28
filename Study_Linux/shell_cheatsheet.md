# Shell Cheatsheet


```bash
#!bin/bash
variabili= 
$"variabile"
$(comando)
$((variabile1 + variabile2))
export MY_VARIABLE="Hello from my variable"
$0                          # script name
$1,2...                     # arguments
# , @ , ?(numero di arguments/ all arguments/exit status)
if [ $# - eq]; then               # if /numero di arguments /equals
elseif else fi 
for arg in "$@"; do             # for loop
done
array=()
array+=(1,"hello")
${array[0]}                     #array as variable
NumberOfNames=${#NAMES[@]}      # list number of elemets 
read -p
$(var:-"not set")               # if var is not set, set it to "not set"
# good example:
MYFILENAME=/home/digby/myfile.txt # Sets the value of MYFILENAME.
FILE=${MYFILENAME##*/} # FILE becomes myfile.txt.
DIR=${MYFILENAME%/*} # DIR becomes /home/digby.
NAME=${FILE%.*} # NAME becomes myfile.
EXTENSION=${FILE##*.} # EXTENSION becomes txt.
```