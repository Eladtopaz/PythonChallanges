from webbot import Browser
import re
import time

# Click on the image to find hint -
# and the next nothing is 44827
# And the url is - http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

# Make a Browser object
web = Browser()
# First number
num = "12345"
# The url
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

# Next number is -
new_num = str(44827)

# Go to the website with that link and new number
web.go_to(link + new_num)

# Search for the pattern and the next number
pattern = re.compile("and the next nothing is (\d+)")


while True:
    # Get the source of a page
    temp = web.get_page_source()
    # Check for the pattern
    match = pattern.search(temp)
    # If didn't found - so we found the last one
    if match == None:
        break
    # If did found - take the new number
    new = match.group(1)
    # And go into his page
    web.go_to(link + new)

# Go to the last page before break
web.go_to(link + new)
# Pause on it
time.sleep(100)


# next hint - Keep doing with the new number
keep_doing = 16044
# Devide by two
devide_by_two = keep_doing / 2
new_num = str(devide_by_two)


# Go to the website with that link and new number
web.go_to(link + new_num)

# Search for the pattern and the next number
pattern = re.compile("and the next nothing is (\d+)")


while True:
    # Get the source of a page
    temp = web.get_page_source()
    # Check for the pattern
    match = pattern.search(temp)
    # If didn't found - so we found the last one
    if match == None:
        break
    # If did found - take the new number
    new = match.group(1)
    # And go into his page
    web.go_to(link + new)

# Go to the last page before break
web.go_to(link + new)
# Pause on it
time.sleep(100)

# Solution: peak.html
# URL: http://www.pythonchallenge.com/pc/def/peak.html
