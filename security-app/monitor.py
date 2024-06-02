from scapy.all import sniff, IP, TCP
import threading

DB_SERVER_IP = '127.0.0.1'
DB_SERVER_PORT = 3306

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet.getlayer(IP)
        tcp_layer = packet.getlayer(TCP)

        if ip_layer.dst == DB_SERVER_IP and tcp_layer.dport == DB_SERVER_PORT:
            print(f"New connection to DB detected from {ip_layer.src}:{tcp_layer.sport}")

def start_sniffing():
    sniff(prn=packet_callback, filter=f"tcp port {DB_SERVER_PORT}", store=0)

sniff_thread = threading.Thread(target=start_sniffing)
sniff_thread.start()
print("Started packet sniffing...")

sniff_thread.join()
