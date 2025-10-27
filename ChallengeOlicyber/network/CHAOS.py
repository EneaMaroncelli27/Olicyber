import subprocess

subprocess.run("tshark -r CHAOS.pcap -T fields -e frame.time_epoch -e tcp.payload  | sort -k1,1n   | cut -f2- > logs.txt",shell=True)


with open('logs.txt', 'r') as f:
    logs = f.readlines()

for l in logs:

    c = bytes.fromhex(l.strip())
    if len(c) > 0 and c != b"\n":
        print(c.decode(),end="")