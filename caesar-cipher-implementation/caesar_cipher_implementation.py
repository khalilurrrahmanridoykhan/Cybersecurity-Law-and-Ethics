def encypt_func(txt, s):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

txt = "ABCdef"
s = 1

print("Text  : " + txt)
print("Shift : " + str(s))
print("Cipher: " + encypt_func(txt, s))