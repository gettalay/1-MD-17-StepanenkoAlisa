from PIL import Image, ImageDraw, ImageFont


def t1():
    filename = '10.jpg'
    with Image.open(filename) as img:
        img.load()
        img_crop = img.crop((200, 400, 600, 900))
        img_crop.show()
        img_crop.save('new_crop.jpg')


def t2():
    otkritka = {
        'первое мая': 'may.jpg',
        'день рождения': 'birthday.jpg'
    }

    card = input('Название праздника: ')
    if card in otkritka:
        img = otkritka[card]
        print(f"Открытка к празднику '{card}':")

        newimg = Image.open(img)
        newimg.show()
    else:
        print('Открытка не найдена')


def t3():
    filename = 'otkritka.jpg'
    with Image.open(filename) as img:
        img.load()
        img_crop = img.crop((200, 400, 600, 950))
        img_crop.show()
        img_crop.save('otkritka_crop.jpg')
        name = input('Введите имя получателя: ')
        draw = ImageDraw.Draw(img_crop)

        text = f'{name}, поздравляю!'
        text_color = {0, 0, 0}
        text_position = (50, img_crop.height - 50)
        font = ImageFont.load("arial.pil")
        draw.text(text_position, text, font=font, fill=text_color)

        img_crop.save('card.jpg')
