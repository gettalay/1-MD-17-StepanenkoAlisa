from PIL import Image, ImageFilter

def z1():
    img = Image.open('10.jpg')
    img.show()
    print(f'Размер: ', img.size, f'. Формат: ', img.format, f'. Цветовая модель: ', img.mode)


def z2():
    img = Image.open('12.jpg')
    reimg = img.thumbnail((img.height / 3, img.width / 3))
    reimg.save(r'Z:\1-МД-17 алгоритмизация\Степаненко\1\11.jpg')

    mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save = (r'Z:\1-МД-17 алгоритмизация\Степаненко\1\12.jpg')

    mirror2 = img.transpose(Image.FLIP_TOP_BOTTOM)
    mirror2.save = (r'Z:\1-МД-17 алгоритмизация\Степаненко\1\13.jpg')
    print()


def z3():
    for i in range(1, 6):
        img = Image.open(f'{i}.jpg')
        filterimg = img.filter(ImageFilter.CONTOUR)
        filterimg.save = (fr'Z:\1-МД-17 алгоритмизация\Степаненко\2\{i}.jpg')
    print()


def z4():
    wm = Image.open('cat.png')
    pos = (0, 0)
    for i in range(1, 6):
        img = Image.open(f'{i}.jpg')
        watermarkimg = img.copy()
        watermarkimg.paste(wm, pos, wm)
        watermarkimg.save = (fr'Z:\1-МД-17 алгоритмизация\Степаненко\2\{i}.jpg')
    print()
