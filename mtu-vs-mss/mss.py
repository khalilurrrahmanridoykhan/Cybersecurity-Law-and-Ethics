from scapy.all import IP, TCP, sr1

def find_mss(destination):
    ip = IP(dst=destination)
    syn = TCP(dport=80, flags="S")
    syn_ack = sr1(ip/syn, timeout=1, verbose=0)

    if syn_ack and TCP in syn_ack:
        options = syn_ack[TCP].options
        for opt in options:
            if opt[0] == "MSS":
                return opt[1]

destination = "8.8.8.8"  # Google's public DNS server
mss = find_mss(destination)
print(f"The MSS size is: {mss}")
