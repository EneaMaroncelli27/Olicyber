import pyshark 

cap = pyshark.FileCapture("net2.pcap", display_filter="eth.type == 0xffff",use_json=True,include_raw=True)
flag = ""
for pkt in cap:
    data = pkt.get_raw_packet()
    flag += data[:1].decode()

print(flag)