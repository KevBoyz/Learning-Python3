from PIL import Image

im = Image.open('gabiru.jpeg')
# print(f'File dimensions: {im.size}')

# Resizing

im_rszd = im.resize(  # The obj need has repatriate for edition did to save
    (int(im.size[0] * 1.1), int(im.size[1] * 1.1))
)

# Handling

im_rszd = im_rszd.rotate(45, expand=True)  # Expand maintain the image full adding borders
im_rszd = im_rszd.transpose(Image.FLIP_LEFT_RIGHT)  # Mirroring

try:
    im_rszd.save('bigger-gabiru.png')  # Convert to png
except ValueError as e:  # unknown file extension
    print(f'Error: {e}')
