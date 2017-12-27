#!/bin/sh
set -x

rm -rf /root/backup/*

# cp -r /var/www/html/* /root/backup/
cp -r /var/www/html/* /root/backup/
rm -rf /var/www/html/*
# cp -r /root/git/raichu.cn/* /var/www/html/
cp -r /root/git/pokemon_vue/dist/* /var/www/html/