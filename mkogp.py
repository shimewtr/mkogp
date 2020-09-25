from PIL import Image, ImageDraw, ImageFont, ImageFilter


def mkogp():
    imageSize = (1200, 800)
    iconSize = (160, 160)
    backgroundColor = (112, 112, 112)
    textColor = (255, 255, 255)
    text = "記事タイトルを入れてください"
    fontSize = 60
    subText = "ブログのタイトルを入れてください"
    subFontSize = 40

    im = Image.new("RGB", imageSize, backgroundColor)

    add_text(im, text, fontSize, textColor, imageSize[0]//2, imageSize[1]//3)
    add_text(im, subText, subFontSize, textColor, imageSize[0]//2, imageSize[1]//6 * 5)

    icon_path = './icon.png'
    icon = Image.open(icon_path).copy()
    icon = icon.resize(size=iconSize, resample=Image.ANTIALIAS)
    mask = Image.new("L", icon.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, icon.size[0], icon.size[1]), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(1))
    icon.putalpha(mask)
    im.paste(icon, (imageSize[0] // 2 - iconSize[0] // 2,
         imageSize[1] // 7 * 4), icon)

    im.save("./image.png")

def add_text(im, text, fontSize, textColor, width, height):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('./MPLUS1p-Regular.ttf', fontSize)
    textWidth, textHeight = draw.textsize(text, font=font)
    textTopLeft = (width - textWidth // 2, height)
    draw.text(textTopLeft, text, fill=textColor, font=font)


if __name__ == '__main__':
    mkogp()
