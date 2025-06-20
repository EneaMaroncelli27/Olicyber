import subprocess


ttl = (subprocess.run(['tshark', '-r', 'llt.pcap', '-Y', '(ip.dst == 172.67.157.96) && (ip.src == 172.19.0.2)', '-T', 'fields', '-e', 'ip.ttl'],capture_output=True).stdout).split(b'\n')[:-7]

for l in ttl:
    print(chr(int(l.strip())), end="")