#!/bin/bash

read current
inOrder=true

for i in {1..100}; do
  read next
  echo "current: $current next: $next"
  if [[ $current -ge $next ]] && [[ -n $next ]]; then
    inOrder=false
    break;
  fi
  current=$next
done

if [[ "$inOrder" = true ]]; then
  echo "All in order!"
else
  echo "Not in order..."
fi
