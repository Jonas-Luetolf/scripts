#!/usr/bin/sh

exp="$(rofi -dmenu -p "Rechner")"
res="$(bc <<< $exp)"
rofi -e "$res"
