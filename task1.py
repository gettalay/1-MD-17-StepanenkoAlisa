from PIL import Image, ImageFilter
import os

inp = r'Z:\1-МД-17 алгоритмизация\Степаненко'
outp = r'Z:\1-МД-17 алгоритмизация\Степаненко\2'
os.makedirs(outp, exist_ok=True)

for file_name in os.listdir(inp):
    input_path = os.path.join(inp, file_name)

    if os.path.isfile(input_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(input_path)

        processed_img = image.filter(ImageFilter.BLUR)

        output_path = os.path.join(outp, file_name)
        processed_img.save(output_path)

print("Обработка изображений завершена.")
