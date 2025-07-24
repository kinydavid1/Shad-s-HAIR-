import os
import platform

def ping(ip):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {param} {ip} > /dev/null 2>&1"
    return os.system(command) == 0

def scan(prefix):
    print(f"🔍 Scan en cours sur le réseau {prefix}.0/24...\n")
    for i in range(1, 255):
        ip = f"{prefix}.{i}"
        if ping(ip):
            print(f"🖥️ Appareil détecté : {ip}")

# --- Lancer le scan ---
prefix = input("Entrez le préfixe IP (ex: 192.168.1) : ")
scan(prefix)
