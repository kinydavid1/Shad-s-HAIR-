import socket
import concurrent.futures
from datetime import datetime

# Ports à scanner et leurs services connus
ports_to_scan = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

# Résultats à enregistrer
results = []

def scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        s.close()
        service = ports_to_scan.get(port, "Inconnu")
        line = f"{ip} : port {port} ouvert ({service})"
        print("🟢 " + line)
        results.append(line)
    except:
        pass

def scan_host(ip):
    for port in ports_to_scan:
        scan(ip, port)

def main():
    prefix = input("🧠 Préfixe IP (ex: 192.168.1) : ")
    print("\n🔍 Scan en cours...\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(1, 255):
            ip = f"{prefix}.{i}"
            executor.submit(scan_host, ip)

    # Sauvegarde des résultats
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"resultats_scan_{now}.txt"
    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")
    print(f"\n✅ Résultats enregistrés dans : {filename}")

main()
