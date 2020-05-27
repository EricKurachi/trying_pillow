from PIL import Image, ImageDraw, ImageFont
import math

image = Image.open("input_image.jpg")
# scale factor between 0.1 - 1
scale_fac = 0.8
char_width = 10
char_height = 18
w, h = image.size
image = image.resize((int(scale_fac * w), int(scale_fac * h * (char_width/char_height))), Image.NEAREST)
w, h = image.size
pixels = image.load()

font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
output_image = Image.new('RGB', (char_width * w, char_height * h), color=(0, 0, 0))
draw = ImageDraw.Draw(output_image)


def get_some_char(sel):
    # chars = "sancaSANCA"[::-1]
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    char_arr = list(chars)
    mul = len(char_arr)/256
    return char_arr[math.floor(sel * mul)]


for i in range(h):
    for j in range(w):
        r, g, b = pixels[j, i]
        grey = int((r/3 + g/3 + b/3))
        pixels[j, i] = (grey, grey, grey)
        draw.text((j * char_width, i * char_height), get_some_char(grey), font=font, fill=(r, g, b))

output_image.save("output_image.png")
