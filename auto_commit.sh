#!/bin/bash

# This file can be run to automatically 
# add, commit and push a file to git

git add .
echo "enter message : " 
read message
git commit -m $message 
git push
