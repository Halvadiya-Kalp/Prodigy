# Network Packet Analyzer

# Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

from scapy.all import sniff, IP, TCP, UDP, ARP

def packet_callback(packet):
    # Analyze packet
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")
    if packet.haslayer(UDP):
        udp_layer = packet.getlayer(UDP)
        print(f"UDP Packet: {udp_layer.sport} -> {udp_layer.dport}")
    if packet.haslayer(ARP):
        arp_layer = packet.getlayer(ARP)
        print(f"ARP Packet: {arp_layer.psrc} -> {arp_layer.pdst}")

def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (e.g., eth0, wlan0): ")
    print(f"Starting packet sniffing on interface {interface}")
    start_sniffing(interface)
