#!/bin/bash
BROWSER="brave"
SEARCHURL="https://www.startpage.com/sp/search?query="
SEARCHNAME="Startpage"

SEARCHSTRING="$(rofi -dmenu -p "$SEARCHNAME" | sed "s/\ /%20/g")"

$BROWSER $SEARCHURL$SEARCHSTRING&
