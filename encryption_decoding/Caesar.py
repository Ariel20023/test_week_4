def caesar_encryption(text,offset):#הצפנה
    res = ""
    text_uniform = text.swapcase()
    for i in range(len(text)):
        if text_uniform[i] == "y" or  text_uniform[i] == "Y":
            res += "a"
        elif text_uniform[i] == "z" or text_uniform[i] == "Z":
            res += "b"
        else:
            res +=chr(ord(text_uniform[i]) + offset)

    return res.swapcase()



def caesar_decoding(text,offset):#פיענוח
    res = ""
    text_uniform = text.swapcase()
    for i in range(len(text)):
        if text_uniform[i] == "a" or text_uniform[i] == "A":
            res += "y"
        elif text_uniform[i] == "b" or text_uniform[i] == "B":
            res += "z"
        else:
            res += chr(ord(text[i]) - offset)

    return res.swapcase()















