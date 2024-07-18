#!/bin/bash
SELECTEDNETWORK="$(echo "$(nmcli -f SSID dev wifi | tail -n +2)" | rofi -p 'Select network' -sep "\n" -dmenu)"
SELECTEDNETWORK=$(echo "$SELECTEDNETWORK" | xargs)

# get network details
info="$(nmcli device wifi list | grep "$SELECTEDNETWORK" -m 1)"
info="${info%"${info##*[![:space:]]}"}"

# check if network needs a password
if [ "${info: -2}" = "--" ]; then
    nmcli dev wifi connect "${SELECTEDNETWORK%"${SELECTEDNETWORK##*[![:space:]]}"}"

else
    # check if the password is already saved
    if  [ -n "$(nmcli -t -f NAME connection show | grep "$SELECTEDNETWORK")" ]; then
        pass="$(nmcli -s -g 802-11-wireless-security.psk connection show "$SELECTEDNETWORK")"

    # get the password from the user
    else        
        pass="$(rofi -dmenu -p 'Enter Password')"

    fi

    # connect to the network
    nmcli dev wifi connect "${SELECTEDNETWORK%"${SELECTEDNETWORK##*[![:space:]]}"}" password $pass 
fi
