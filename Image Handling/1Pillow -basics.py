from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# print(f'File dimensions: {im.size}'


def resize(im):
    im_rszd = im.resize(  # The obj need has repatriate for edition did to save
        (int(im.size[0] * 1.1), int(im.size[1] * 1.1))
    ).show()


def rotate(im):
    im = im.rotate(45, expand=True)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return im


def sharp(im):
    im = ImageEnhance.Sharpness(im)
    return im.enhance(7)


def color(im):
    im = ImageEnhance.Color(im)
    return im.enhance(1.3)


def contrast(im):
    im = ImageEnhance.Contrast(im)
    return im.enhance(1.1)


def brightness(im):
    im = ImageEnhance.Brightness(im)
    return im.enhance(0.99)


def save(im):
    try:
        im.save('gabiru(1).png')  # Convert to png
    except ValueError as e:  # unknown file extension
        print(f'Error: {e}')


def compare(im):
    mod_im = im.copy()
    mod_im = drawing('KevBoyz', 30, 5, '#000000')
    mod_im = sharp(mod_im)
    mod_im = color(mod_im)
    mod_im = contrast(mod_im)
    mod_im = brightness(mod_im)


    plt.figure(facecolor='#cccccc')

    plt.suptitle('\n\n\nImages comparison')

    plt.subplot(1, 2, 1)
    plt.title('Original')
    plt.imshow(im)

    plt.subplot(1, 2, 2)
    plt.title('Edited')
    plt.imshow(mod_im)

    plt.show()


def drawing(text, size, padding, color='#ffffff'):  # 15px size font for 100 px size axis
    im = Image.open('gabiru.jpeg')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(r'C:\Windows\Fonts\consolab.ttf', size=size)
    pxlen = len(text) * size
    print(pxlen)
    x = ((im.size[0] - pxlen) + pxlen / 2.5) - padding + 5
    y = im.size[1] / 10 - 15
    if y < size + padding:
        while y < size + padding:
            y += padding
    draw.text((x, im.size[1] - y), text, font=font, fill=color)
    return im


compare(Image.open('gabiru.jpeg'))
