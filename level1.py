# Level 1

sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# # # hint = {
# # #     "k": "m",
# # #     "o": "q",
# # #     "e": "g"
# # # }
# Every letter become the next second letter

# ord(c) make c to number
# chr(5) make 5 to digit


def dechiper(s):
    deciphered_string = ""
    for letter in s:
        if letter == " " or letter == "." or letter == "'" or letter == "(" or letter == ")":  # Special letters in the string
            deciphered_string += letter          # Add to result
        elif letter == "y":                             # y/z + 2 won't become a/b so - take care that
            deciphered_string += "a"
        elif letter == "z":
            deciphered_string += "b"
        else:
            deciphered_string += chr(ord(letter) + 2)  # Transfer letter to it number, then add 2 and transfer to letter again
    print(deciphered_string)   # Print the result


dechiper(sentence)

# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

def dechiper2(s):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")  # Transfer a to c, b to d and so on
    print(s.translate(table))


# Apply to the url
dechiper2("map")
