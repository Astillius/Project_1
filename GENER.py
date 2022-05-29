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
    main_spt = input("Ключ: ")
    spt = main_spt.split(" ")
    print("═" * 5, "Виды шифрования:", "═" * 5, "\n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов")
    option = int(input("Выберите вид шифрования: "))
    if option == 1:
        letcrpt(spt, info)
    if option == 2:
        grpcrpt(spt, info)
    if option == 3:
        wordcrpt(spt, info)

def decrypt():
    info = input("Введи текст сообщениия, которое необходимо расшифровать: ")
    main_spt = input("Ключ, с помощью которого было зашифровано сообщение: ")
    spt = main_spt.split(" ")
    print("═" * 5, "Способ, с помощью которого было защифровано сообщение:", "═" * 5 , "\n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов")
    option = int(input("Способ шифрования: "))
    if option == 1:
        decrypt_let(spt, info)
    if option == 2:
        decrypt_grp(spt, info)
    if option == 3:
        decrypt_word(spt, info)

def driver_code(spt, info):
    code = ''
    structure = ''
    size_of_spt = len(spt)
    numeration = len(info)
    for i in range(0, numeration, size_of_spt):
        structure = [info[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            code += str(structure[size_of_spt - int(spt[j]) - 1])
    return code


def letcrpt(spt, info):
    size_of_spt = len(spt)
    numeration = len(info)
    if numeration % size_of_spt != 0:
        for i in range(size_of_spt - (numeration % size_of_spt)):
            info += str("0")
    print(driver_code(spt, info))


def grpcrpt(spt, info):
    size_of_spt = len(spt)
    amount_of_sym = int(input("На какие группы нужно разбить (кол-во символов)? "))
    exit_t = [info[i:i + amount_of_sym] for i in range(0, len(info), amount_of_sym)]
    if len(exit_t[-1]) != amount_of_sym:
        for i in range(amount_of_sym - (len(exit_t[-1]) % amount_of_sym)):
            exit_t[-1] += str("0")
    if len(exit_t) != size_of_spt:
        for i in range(size_of_spt - (len(exit_t) % size_of_spt)):
            exit_t.append("0" * amount_of_sym)
    print(driver_code(spt, exit_t))


#def wordcrpt(spt, info):

#def decrypt_let(spt, info):

#def decrypt_grp(spt, info):

#def decrypt_word(spt, info):


while True:
    Greetings()
