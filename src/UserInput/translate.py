def translate(frase):
    translation = ""
    for letter in frase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Insira uma frase:")))