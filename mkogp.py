import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

EXPORT_PATH = os.environ['EXPORT_PATH']

def mkdirs():
    os.makedirs(EXPORT_PATH, exist_ok=True)

def mkogp():
    image_size = (1200, 630)
    icon_size = (160, 160)
    background_color = (112, 112, 112)
    text_color = (255, 255, 255)
    text = '記事タイトルを入れてください'
    font_size = 60
    font_medium_path = './fonts/MPLUS1p-Medium.ttf'
    sub_text = "ブログのタイトルを入れてください"
    subfont_size = 40
    font_light_path = './fonts/MPLUS1p-Light.ttf'
    icon_path = './assets/icon.png'

    im = Image.new('RGB', image_size, background_color)

    add_text(im, text, font_size, font_medium_path,
             text_color, image_size[0]//2, image_size[1]//4)
    add_text(im, sub_text, subfont_size, font_light_path,
             text_color, image_size[0]//2, image_size[1]//6 * 5)
    add_icon(im, image_size, icon_size, icon_path)

    im.save(EXPORT_PATH + '/image.png')


def add_icon(im, image_size, icon_size, icon_path):
    icon = Image.open(icon_path).copy()
    icon = icon.resize(size=icon_size, resample=Image.ANTIALIAS)
    mask = Image.new("L", icon.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, icon.size[0], icon.size[1]), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(1))
    icon.putalpha(mask)
    im.paste(icon, (image_size[0] // 2 - icon_size[0] // 2,
                    image_size[1] // 7 * 4), icon)


def add_text(im, text, font_size, fontPath, text_color, width, height):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(fontPath, font_size)
    textWidth, _ = draw.textsize(text, font=font)
    textTopLeft = (width - textWidth // 2, height)
    draw.text(textTopLeft, text, fill=text_color, font=font)


if __name__ == '__main__':
    mkdirs()
    mkogp()
