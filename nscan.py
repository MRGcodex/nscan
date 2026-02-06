#!/usr/bin/env python3

import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}
███╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║███████╗██║     ███████║██╔██╗ ██║
██║╚██╗██║╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚████║███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

Option-based Nmap
Developed by MRGcodex
"""

MENU = f"""
{Fore.YELLOW}Select Scan Type:
{Fore.GREEN}1){Style.RESET_ALL} Ping Scan (Host Discovery)
{Fore.GREEN}2){Style.RESET_ALL} Quick Scan
{Fore.GREEN}3){Style.RESET_ALL} Full Port Scan
{Fore.GREEN}4){Style.RESET_ALL} Service & Version Scan
{Fore.GREEN}5){Style.RESET_ALL} OS Detection
{Fore.GREEN}6){Style.RESET_ALL} Aggressive Scan
{Fore.GREEN}7){Style.RESET_ALL} Vulnerability Scripts
{Fore.GREEN}8){Style.RESET_ALL} UDP Scan
{Fore.GREEN}9){Style.RESET_ALL} Custom Nmap Arguments
{Fore.RED}0){Style.RESET_ALL} Exit
"""

def run(cmd):
    print(f"\n{Fore.CYAN}[+] Running:{Style.RESET_ALL} {cmd}\n")
    os.system(cmd)

def main():
    os.system("clear")
    print(BANNER)

    target = input(f"{Fore.YELLOW}Enter Target IP / Range / Domain: {Style.RESET_ALL}").strip()
    if not target:
        print("No target provided.")
        sys.exit(1)

    while True:
        print(MENU)
        choice = input(f"{Fore.YELLOW}Choose option: {Style.RESET_ALL}")

        if choice == "1":
            run(f"nmap -sn {target}")
        elif choice == "2":
            run(f"nmap -T4 -F {target}")
        elif choice == "3":
            run(f"nmap -p- {target}")
        elif choice == "4":
            run(f"nmap -sV {target}")
        elif choice == "5":
            run(f"nmap -O {target}")
        elif choice == "6":
            run(f"nmap -A {target}")
        elif choice == "7":
            run(f"nmap --script vuln {target}")
        elif choice == "8":
            run(f"nmap -sU {target}")
        elif choice == "9":
            args = input("Enter custom nmap arguments: ")
            run(f"nmap {args} {target}")
        elif choice == "0":
            print("Exiting Nscan...")
            break
        else:
            print("Invalid option!")

        input("\nPress Enter to continue...")
        os.system("clear")
        print(BANNER)

if __name__ == "__main__":
    main()