# Level7

from PIL import Image
import os

# Open the source code, find only 1 thing - the oxygen picture.
# Download the photo and keep it in the same directory as this one

# Initialize absolute path for later use
dirname = os.path.dirname(__file__)

# Take the oxygen picture
oxygen = Image.open(os.path.join(dirname, r'oxygen.png'))

# Size of the picture (can print by - print(oxygen))
size = width, height = 629, 95

# The line of the grey scale
y = 48
# x = 0 - 607, Incrase of 7 evey time
my_list = []

# Run on th grey scale
for x in range(0, 607, 7):
    # Take the pixel RGB
    my_list.append(oxygen.getpixel((x, y))[0])

# Change it to a char by chr
my_list = "".join([chr(n) for n in my_list])
# Print result
print(my_list)

# Next hint - smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

my_list2 = [105, 110, 116, 101, 103, 114, 105, 116, 121]
my_list2 = "".join([chr(n) for n in my_list2])
print(my_list2)

# Solution: integrity. URL: http://www.pythonchallenge.com/pc/def/integrity.html
