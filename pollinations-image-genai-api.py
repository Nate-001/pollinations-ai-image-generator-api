import requests
import random
import os

os.makedirs('generated_images', exist_ok=True)

def download_image(prompt, counter):
    seed = random.randint(1, 1000000)
    url = f"https://image.pollinations.ai/prompt/{prompt}?seed={seed}"
    response = requests.get(url)
    filename = f'generated_images/damaged_house_{counter:03d}.jpg'
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'Image {counter} downloaded as {filename} with seed {seed}!')

for x in range(500):
    download_image("hyperrealistic_damaged_house", x)
