#!/bin/bash

echo "[+] Installing Nscan requirements..."

if command -v pkg >/dev/null 2>&1; then
    pkg update -y
    pkg install -y python nmap
elif command -v apt >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y python3 python3-pip nmap
fi

pip install -r requirements.txt

chmod +x nscan.py
chmod +x run.sh

echo "[✓] Installation complete"