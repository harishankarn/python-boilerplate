#!/bin/bash

# This file can be run to automatically 
# add, commit and push a file to git

git add .
echo "enter message :"
git commit -m $1
git push
