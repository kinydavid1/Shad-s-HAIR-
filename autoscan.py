import socket
import fcntl
import struct
import os
from scapy.all import ARP, Ether, srp

def get_ip_address():
    interfaces = os.listdir('/sys/class/net/')
    for interface in interfaces:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip = socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', bytes(interface[:15], 'utf-8'))
            )[20:24])
            if ip.startswith('192.') or ip.startswith('10.') or ip.startswith('172.'):
                return ip
        except:
            continue
    return None

def scan_network(ip_prefix):
    target_ip = ip_prefix + ".1/24"
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]
    print(f"\n📡 Appareils détectés sur {target_ip} :\n")
    for sent, received in result:
        print(f"🖥️ IP : {received.psrc}  |  MAC : {received.hwsrc}")

# --- Début du programme ---
ip = get_ip_address()

if ip:
    ip_prefix = ".".join(ip.split(".")[:3])
    print(f"🛜 IP locale détectée : {ip}")
    scan_network(ip_prefix)
else:
    print("❌ Impossible de détecter l'adresse IP locale.")
