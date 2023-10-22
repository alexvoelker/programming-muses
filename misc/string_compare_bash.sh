#!/bin/bash

echo "Enter the first string: "
read str1
echo "Enter the second string: "
read str2

echo ""

if [[ "$str1" -eq "$str2" ]]; then 
  echo "True: strings match!" 
else
  echo "False: strings do NOT match."
fi

