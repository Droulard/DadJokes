#!/bin/sh

pip3 install -r requirements.txt
mkdir -p ~/.Python/Dad/
mv ./* ~/.Python/Dad/
echo "source ~/.Python/Dad/Dad.sh" >> ~/.zshrc

