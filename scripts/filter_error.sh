#!/bin/bash 
list=$1
search_path=.
if [ "$list" == "list" ]; then
    grep -R -e 'failures=\"[1-9]\"' -e 'errors=\"[1-9]\"' $search_path 
    echo "================================="
    grep -Rl -e 'failures=\"[1-9]\"' -e 'errors=\"[1-9]\"' $search_path 
    echo "================================="
else
    grep -R -e 'failures=\"[1-9]\"' -e 'errors=\"[1-9]\"' $search_path | wc -l
fi
