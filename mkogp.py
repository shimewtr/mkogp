from PIL import Image, ImageDraw, ImageFont


def mkogp():
    imageSize = (1200, 800)
    backgroundColor = (112, 112, 112)
    textColor = (255, 255, 255)
    fontSize = 50
    text = "画像に埋め込むテキストを入力してください"

    im = Image.new("RGB", imageSize, backgroundColor)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('./MPLUS1p-Regular.ttf', fontSize)
    textWidth, textHeight = draw.textsize(text, font=font)
    textTopLeft = (imageSize[0]//2-textWidth//2,
                   imageSize[1]//2-textHeight//2)
    draw.text(textTopLeft, text, fill=textColor, font=font)
    im.save("./image.png")


if __name__ == '__main__':
    mkogp()
