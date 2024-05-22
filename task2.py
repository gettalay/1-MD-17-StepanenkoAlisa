import os
from PIL import Image

source = r'Z:\1-МД-17 алгоритмизация\Степаненко'
destination_folder = r'Z:\1-МД-17 алгоритмизация\Степаненко\2'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source):
    if filename.endswith(".jpg") or filename.endswith(".png"):

        image_path = os.path.join(source, filename)
        image = Image.open(image_path)
        image = image.rotate(90)
        image = image.resize((300, 300))
        destination_path = os.path.join(destination_folder, filename)
        image.save(destination_path)

print("Изображения обработаны и сохранены в указанной папке.")
