# Nscan

> Advanced option‑based Nmap framework  
> Real scanning • No fake output • Menu driven  
> Developed by **MRGcodex**

---

## Overview

Nscan is a professional, menu‑driven interface for **real Nmap**.  
Designed for penetration testers, security researchers, and learners who want full Nmap power **without memorizing commands**.

---

## Core Features

• Real Nmap engine (not simulated)  
• Option‑based execution  
• Full port scanning  
• Service & version detection  
• OS fingerprinting  
• Vulnerability detection scripts  
• UDP scanning  
• Custom argument execution  
• Android (Termux) compatible  
• Linux & macOS support  

---

## Requirements

nmap  
python3  
pip  

---

## Installation (Android / Termux)

pkg update -y  
pkg install git python nmap -y  
termux-setup-storage  

git clone https://github.com/YOURUSERNAME/Nscan.git  
cd Nscan  

bash install.sh  

---

## Installation (Linux / macOS)

sudo apt update  
sudo apt install git python3 python3-pip nmap -y  

git clone https://github.com/YOURUSERNAME/Nscan.git  
cd Nscan  

bash install.sh  

---

## Execution

cd Nscan  
bash run.sh  

OR

python3 nscan.py  

---

## Usage Flow

Enter target:

192.168.1.1  
192.168.1.0/24  
scanme.nmap.org  

Select scan mode:

1  Host Discovery  
2  Quick Scan  
3  Full Port Scan  
4  Service & Version Detection  
5  OS Detection  
6  Aggressive Scan  
7  Vulnerability Scripts  
8  UDP Scan  
9  Custom Nmap Arguments  
0  Exit  

Scan runs immediately using **real nmap**.

---

## Custom Scan Mode

Select option:

9  

Enter arguments:

-sS -Pn -T4 --open  

---

## Internal Network Scan Example

Target:

192.168.1.0/24  

Option:

1  

---

## Permissions

chmod +x install.sh  
chmod +x run.sh  
chmod +x nscan.py  

---

## Update

cd Nscan  
git pull  

---

## Uninstall

rm -rf Nscan  

---

## Legal Disclaimer

This tool is intended for **authorized security testing and educational use only**.  
Unauthorized scanning of networks or systems is illegal.

---

## Author

MRGcodex

---

## Status

Stable • Actively usable • Community expandable
