#!/bin/bash
# Bash scripts that sends  POST request to  given URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
