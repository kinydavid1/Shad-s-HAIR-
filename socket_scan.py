import socket
import concurrent.futures

def scan_ip(ip, port=80):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        s.close()
        print(f"🟢 Appareil actif (port {port} ouvert) : {ip}")
    except:
        pass

def main():
    prefix = input("Entrez le préfixe IP (ex: 192.168.1) : ")
    port = int(input("Port à tester (ex: 80 ou 22) : "))
    print(f"\n🔍 Scan du réseau {prefix}.0/24 sur le port {port}...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(1, 255):
            ip = f"{prefix}.{i}"
            executor.submit(scan_ip, ip, port)

main()
