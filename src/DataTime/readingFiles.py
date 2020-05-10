
people_file = open("/home/thiago/Documentos/arquivo.txt", "r")
for people in people_file.readlines():
    print(people)
people_file.close()