import matplotlib.pyplot as plt
import math

def to_signed(b):
    return b - 256 if b >= 128 else b

x, y = 0, 0
coords = [(x, y)]
click_scroll = [(False,False)]
with open("reports.txt") as f:
    print("Lettura dati da reports.txt...")
    for line in f:
        line = line.strip().replace(" ", "").replace('\"', '')
        if len(line) < 6:  # report troppo corto
            continue
        try:
            
            data = bytes.fromhex(line)
            
        except ValueError:
            continue

        print(data)
        if len(data) < 3:
            continue
        dx = to_signed(data[1])
        dy = to_signed(data[2])
        x += dx
        y += dy
        if data[0] == 0x00:

            coords.append((math.nan, math.nan))
            continue
        coords.append((x, y))


xs, ys = zip(*coords)
plt.figure(figsize=(6,6))
plt.plot(xs, ys, '-', linewidth=1)
plt.title("Tracciamento movimento mouse (da USB HID)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.gca().invert_yaxis()
plt.show()
