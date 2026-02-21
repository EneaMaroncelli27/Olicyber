from PIL import Image, ImageDraw, ImageFont
import os
import random
from tqdm import trange

def get_image():
    images = os.listdir("enc")
    image = random.choice(images)
    image = Image.open(f'enc/{image}')
    return image

def remove_noise(image):
    for x in range(image.width):
        for y in range(image.height):
            p = image.getpixel((x,y))
            new = []
            for c in p:
                rnd = random.randint(0, 255)
                if c - rnd < 0:
                    new.append(((c - rnd) + 256) % 256)
                else:
                    new.append(c - rnd)
            p = tuple(new)       
            image.putpixel((x,y), p)

for i in trange(256):
    img = Image.open("enc/output.bin")
    random.seed(i)
    remove_noise(img)
    img.save(f"prove/prova{i}.png")
