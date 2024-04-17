from PIL import Image

img = Image.open('12.jpg')
img.show()
print(img.size, img.format, img.mode)
reimg = img.resize((420, 240))
reimg.save(r'Z:\1-МД-17 алгоритмизация\Степаненко\1\13.jpg')
new = img.transpose(Image.FLIP_LEFT_RIGHT)
new.save = (r'Z:\1-МД-17 алгоритмизация\Степаненко\1\14.jpg')
