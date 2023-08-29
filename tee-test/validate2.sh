#!/bin/bash

read current
read next
inOrder=true

while [[ -n $next ]]; do
  # echo "current: $current next: $next"
  if [[ $current -ge $next ]]; then
    inOrder=false
    break;
  fi
  current=$next
  read next
done

if [[ "$inOrder" = true ]]; then
  echo "All in order!"
else
  echo "Not in order..."
fi
