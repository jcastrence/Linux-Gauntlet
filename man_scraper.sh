#!/bin/bash

com_file="commands.txt"
man_file="descriptions.txt"

if [ ! -f "$com_file" ]; then
  echo "Error: "$com_file" not found"
  exit 1
fi

> "$man_file"
while IFS= read -r line; do
  man "$line" | sed -n '4p' >> "$man_file"
done < "$com_file"


