# Level6


import zipfile
import re

# Open source code to find:
# Hint : zip
# Download the zip file writing the url: http://www.pythonchallenge.com/pc/def/channel.zip
# Find zip file with 910 files, one of them is "readme" file, in the file there is another hints:
# Hint1 = start from 90052
# Hint2 = answer is inside the zip

# Open the file "90052.file" to find:
# Next nothing is 94191.
# This is another "The next nothing is"


# First number
num = '90052'
# Pattern
pattern = re.compile("Next nothing is (\d+)")
# Zip file
archive = zipfile.ZipFile("channel.zip", 'r')

while True:
    # Get the content of the next txt file
    content = archive.read(num+'.txt').decode("utf-8")
    # Search for the pattern on it
    match = pattern.search(content)
    # Last txt file
    if match == None:
        print(content)
        break
    # If not - take it comment
    num = match.group(1)

# Hint = collect the comments.

# Redo the whole thing but collect the comments.
# List of comments
comments = []
num = '90052'

while True:
    # Get the content of the next txt file
    content = archive.read(num+'.txt').decode("utf-8")
    # Append it comment to the list
    comments.append(archive.getinfo(num+".txt").comment.decode("utf-8"))
    # Search for the pattern on it
    match = pattern.search(content)
    # Last txt file
    if match == None:
        break
    # If not - take it comment
    num = match.group(1)

# Print the comments
print("".join(comments))

# Hint: Hockey. lead to url: http://www.pythonchallenge.com/pc/def/hockey.html
# Hint: it's in the air. look at the letters.
# Solution: oxygen. url: http://www.pythonchallenge.com/pc/def/oxygen.html.
