def Greetings():
    print("═" * 50)
    print("Алоха! Я - разум по шифрованию текстов.\nВ мой перечень услуг входит:")
    print("1 - Шифровка. \n2 - Расшифровка.")
    while True:
        start = input("Выбери нужную тебе функцию: ")
        if not start.isnumeric():
            print("Вы ввели не число. Введите корректные данные.")
        elif not 0 <= int(start) <= 2:
            print("Вы ввели число вне числового диапазона")
        else:
            if int(start) == 1:
                crypt()
                return 0
            else:
                decrypt()
                return 0


def crypt():
    info = input("Введи текст сообщениия, которое необходимо защифровать: ")
    print("═" * 5, "Введите ключ, с помощью которого будет шифроваться текст. Например: '1 3 0 2'", "═" * 5)
    main_spt = input("Ключ: ")
    spt = main_spt.split(" ")
    print("═" * 5, "Виды шифрования:", "═" * 5,
        "\n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов")
    option = int(input("Выберите вид шифрования: "))
    if int(option) == 1:
        letcrpt(spt, info)
    elif int(option) == 2:
        grpcrpt(spt, info)
    elif int(option) == 3:
        wordcrpt(spt, info)


def decrypt():
    info = input("Введи текст сообщениия, которое необходимо расшифровать: ")
    main_spt = input("Ключ, с помощью которого было зашифровано сообщение: ")
    spt = main_spt.split(" ")
    print("═" * 5, "Способ, с помощью которого было защифровано сообщение:", "═" * 5,
          "\n1 - Символьное шифрование.\n2 - Шифрование группы.\n3 - Шифрование слов")
    option = input("Способ шифрования: ")
    while True:
        if not option.isnumeric():
            print("Вы ввели не число. Введите корректные данные.")
        elif not 0 <= int(option) <= 3:
            print("Вы ввели число вне числового диапазона")
        else:
            if int(option) == 1:
                decrypt_let(spt, info)
            elif int(option) == 2:
                decrypt_grp(spt, info)
            elif int(option) == 3:
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
    return spt, info


def grpcrpt(spt, info):
    size_of_spt = len(spt)
    while True:
        amount_of_sym = input("На какие группы нужно разбить (кол-во символов)? ")
        if not amount_of_sym.isnumeric():
            print("Вы ввели не число. Введите корректные данные.")
        else:
            amount_of_sym = int(amount_of_sym)
            exit_t = [info[i:i + amount_of_sym] for i in range(0, len(info), amount_of_sym)]
            if len(exit_t[-1]) != amount_of_sym:
                for i in range(amount_of_sym - (len(exit_t[-1]) % amount_of_sym)):
                    exit_t[-1] += str("0")
            if len(exit_t) != size_of_spt:
                for i in range(size_of_spt - (len(exit_t) % size_of_spt)):
                    exit_t.append("0" * amount_of_sym)
            print(driver_code(spt, exit_t))
            return spt, info


def wordcrpt(spt, info):
    size_of_spt = len(spt)
    exit_t = info.split(" ")
    if len(exit_t) != size_of_spt:
        for i in range(size_of_spt - (len(exit_t) % size_of_spt)):
            exit_t.append("0" * 5)
    numerate = len(exit_t)
    block = ''
    code = ''
    for i in range(0, numerate, size_of_spt):
        block = [exit_t[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            code += str(block[size_of_spt - int(spt[j]) - 1])
            code += " "
    print(code)
    return spt, info


# def decrypt_let(spt, info):

# def decrypt_grp(spt, info):

# def decrypt_word(spt, info):


flag = True
if flag == True:
    Greetings()
    flag = False
