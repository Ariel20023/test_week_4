

def fence_encryption(text):# הצפנה
    zugi_letter = ""
    ezugi_letter = ""
    encryption = ""
    for i in range(0,len(text) - 1 ,2):
        zugi_letter += text[i]
        ezugi_letter += text[i+1]
    encryption = zugi_letter + ezugi_letter
    if len(text) % 2 != 0 :
        encryption += text[len(text) - 1]
    return encryption




def fence_decoding(text):#פיענוח
    decoding = ""
    middle = len(text) //2
    for i in range(middle):
        decoding += text[i] + text[middle + i]
    if len(text) % 2 != 0 :
        decoding += text[len(text) - 1]
    return decoding






















































