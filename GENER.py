def Greetings():
    print("═" * 50)
    print("Алоха! Я - разум по шифрованию текстов.\nВ мой перечень услуг входит:")
    print("1 - Шифровка. \n2 - Расшифровка.")
    start = int(input("Выбери нужную тебе функцию: "))
    if start == 1:
        crypt()

def crypt():
    info = input("Введи текст сообщениия, которое необходимо защифровать: ")
    print("═" * 5, "Введите ключ, с помощью которого будет шифроваться текст. Например: '1 3 0 2'", "═" * 5)
    main_key = input("Ключ: ")
    spt = main_key.split(" ")
    key = []
    for e in key:
        key.append(int(e))
    print("═" * 5, "Виды шифрования: \n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов")
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


while True:
    Greetings()