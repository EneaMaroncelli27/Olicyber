import pyshark

pcap = pyshark.FileCapture("flag-interceptor.pcap")# diamo a pcap il valore del file 
flags = {} # dizionario 
for packet in pcap:
    if hasattr(packet,"tcp") and packet.tcp.dstport == "5555" and hasattr(packet.tcp, "payload"): #verifichaimo che i pacchetti siano di un certo tipo usando filtri
        print(bytes.fromhex(packet.tcp.payload[:2]))
        src = packet.ip.src
        if not (src in flags.keys()):
            flags[src] = b""    # in caso non esiste la chiave la creiamo  
        flags[src] += bytes.fromhex(packet.tcp.payload[:2]) # gli diamo un valore 
for flag in flags.values():
    if flag.decode().startswith("flag{") and flag.decode()[-1] == "}":
        print(flag.decode())