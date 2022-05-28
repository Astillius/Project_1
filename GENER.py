def Greetings():
    print("═" * 50)
    print("Алоха! Я - разум по шифрованию текстов.\nВ мой перечень услуг входит:")
    print("1 - Шифровка. \n2 - Расшифровка.")
    start = int(input("Выбери нужную тебе функцию: "))
    if start == 1:
        crypt()
    else:
        decrypt()

def crypt():
    info = input("Введи текст сообщениия, которое необходимо защифровать: ")
    print("═" * 5, "Введите ключ, с помощью которого будет шифроваться текст. Например: '1 3 0 2'", "═" * 5)
    main_key = input("Ключ: ")
    spt = main_key.split(" ")
    key = []
    for e in key:
        key.append(int(e))
    print("═" * 5, "Виды шифрования: \n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов", "═" * 5)
    option = int(input("Выберите вид шифрования: "))
    if option == 1:
        letcrpt(key, info)
    if option == 2:
        grpcrpt(key, info)
    if option == 3:
        wordcrpt(key, info)
def letcrpt(key, info):

def grpcrpt(key, info):

def wordcrpt(key, info):

def decrypt():
    info = input("Введи текст сообщениия, которое необходимо расшифровать: ")
    main_key = input("Ключ, с помощью которого было зашифровано сообщение: ")
    spt = main_key.split(" ")
    key = []
    for e in key:
        key.append(int(e))
    print("═" * 5, "Способ, с помощью которого было защифровано сообщение: \n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов", "═" * 5)
    option = int(input("Способ шифрования: "))
    if option == 1:
        decrypt_let(key, info)
    if option == 2:
        decrypt_grp(key, info)
    if option == 3:
        decrypt_word(key, info)
def decrypt_let(key, info):

def decrypt_grp(key, info):

def decrypt_word(key, info):


while True:
    Greetings()