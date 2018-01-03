# pr1
from PIL import Image, ImageDraw, ImageFont, ImageColor


def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('c:/windows/fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, heigth = img.size
    draw.text((width - 30, 0), '1', font=myfont, fill=fillcolor)
    img.save('myimg.jpg', 'jpeg')
    return 0


if __name__ == '__main__':
    image = Image.open('./image.jpg')
    add_num(image)
