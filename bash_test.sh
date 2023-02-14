#!/bin/bash


intro_string = "Hello, World!"
echo $intro_string

#readonly $intro_string
#intro_string = "123"
#echo $intro_string
unset intro_string
echo intro_string

while IFS= read -r line; do 
  echo "$line"
done <filename.txt

setAge() {
    local AGE=25
    echo "Local Variable Age: $AGE"
}
AGE=40
setAge
echo "Global Age: $AGE"

# Single-line comments
#
# ...

: '
Multiline comment example
example 2
example 3
'

echo "123"


