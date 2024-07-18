#!/bin/bash

TERM="alacritty -e"

KNOWN_HOSTS_FILE="$HOME/.ssh/known_hosts"

# Check if the known_hosts file exists
if [[ ! -f "$KNOWN_HOSTS_FILE" ]]; then
    echo "known_hosts file not found at $KNOWN_HOSTS_FILE"
    exit 1
fi

# Extract unique hosts from the known_hosts file
HOSTS=$(awk '{print $1}' "$KNOWN_HOSTS_FILE" | cut -d',' -f1 | sort | uniq)

SELECTED_HOST=$(echo "$HOSTS" | rofi -dmenu -p "Select SSH Host")

# Check if a host was selected
if [[ -z "$SELECTED_HOST" ]]; then
    echo "No host selected"
    exit 1
fi

USER=$(rofi -dmenu -p "Username:")

# check if a username was selected
if [[ -z "$USER" ]]; then
    echo "No Username entered"
    exit 1
fi

# open a terminal emulator and conntect via ssh
$TERM ssh "$USER"@"$SELECTED_HOST" 
