#!/bin/bash
SELECTEDNETWORK="$(echo "$(nmcli -f SSID dev wifi | tail -n +2)" | rofi -p 'Select network' -sep "\n" -dmenu)"

echo $SELECTEDNETWORK

info="$(nmcli device wifi list | grep "$SELECTEDNETWORK" -m 1)"
info="${info%"${info##*[![:space:]]}"}"

if [ "${info: -2}" = "--" ]; then
    nmcli dev wifi connect "${SELECTEDNETWORK%"${SELECTEDNETWORK##*[![:space:]]}"}"

else
    pass="$(rofi -dmenu -p 'Enter Password')"
    nmcli dev wifi connect "${SELECTEDNETWORK%"${SELECTEDNETWORK##*[![:space:]]}"}" password $pass 
fi
