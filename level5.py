# Level5

import pickle
from urllib.request import urlopen


# Hint - pronounce it
# Open source code to find: "banner.p"
# Click on it to find mess

# Open the mess in the url source code
raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

# Read the mess with pickle lib
data = pickle.load(raw)

# print(data) - When you do this you find a lot of tuples

# Take the first index in the tuple and multipe by the second
# For every raw (x is a raw every other loop)
for x in data:
    print("".join([key * val for key, val in x]))

# Solution: channel. URL: http://www.pythonchallenge.com/pc/def/channel.html