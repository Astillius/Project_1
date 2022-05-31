def Greetings():
    print("═" * 50, "Алоха! Я - разум по шифрованию текстов", "В мой перечень услуг входит:", "1 - Шифровка.", "2 - Расшифровка.", sep = "\n")
    while True:
        start = input("Выбери нужную тебе функцию: ")
        if not start.isnumeric():
            print("Вы ввели не число. Введите корректные данные.")
        elif not 0 < int(start) <= 2:
            print("Вы ввели число вне числового диапазона")
        else:
            if int(start) == 1:
                return crypt()
            else:
                return decrypt()


def crypt():
    info = input("Введи текст сообщениия, которое необходимо защифровать: ")
    print("═" * 5, "Введите ключ, с помощью которого будет шифроваться текст. Например: '1 3 0 2' (вводить через пробелы)", "═" * 5)
    spt = input("Ключ: ").split(" ")
    print("═" * 5, "Виды шифрования:", "═" * 5, "1 - Символьное шифрование.", "2 - Шифрование группы.", "3 - Шифрование слов", sep = "\n")
    while True:
        option = input("Выберите вид шифрования: ")
        if not option.isnumeric():
            print("Вы ввели не число. Введите корректные данные.")
        elif not 0 < int(option) <= 3:
            print("Вы ввели число вне числового диапазона")
        if int(option) == 1:
            return letcrpt(spt, info)
        elif int(option) == 2:
            return grpcrpt(spt, info)
        elif int(option) == 3:
            return wordcrpt(spt, info)


def decrypt():
    info = input("Введи текст сообщениия, которое необходимо расшифровать: ")
    spt = input("Ключ, с помощью которого было зашифровано сообщение: ").split(" ")
    print("═" * 5, "Способ, с помощью которого было защифровано сообщение:", "1 - Символьное шифрование.", "2 - Шифрование группы.", "3 - Шифрование слов", sep = "\n")
    while True:
        option = input("Способ шифрования: ")
        if not option.isnumeric():
            print("Вы ввели не число. Введите корректные данные.")
        elif not 0 <= int(option) <= 3:
            print("Вы ввели число вне числового диапазона")
        else:
            if int(option) == 1:
                return decrypt_let(spt, info)
            elif int(option) == 2:
                return decrypt_grp(spt, info)
            elif int(option) == 3:
                return decrypt_word(spt, info)


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


def driver_code_decrypt(spt, info):
    size_of_spt = len(spt)
    numeration = len(info)
    space = ''
    code = ''
    for i in range(0, numeration, size_of_spt):
        space = [info[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            code += str(space[size_of_spt - int(spt[j]) - 1])
    code = code.replace("0", "")
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
    space = ''
    code = ''
    for i in range(0, numerate, size_of_spt):
        space = [exit_t[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            code += str(space[size_of_spt - int(spt[j]) - 1])
            code += " "
    print(code)
    return spt, info


def decrypt_let(spt, info):
    for i in range(len(spt) // 2):
        spt[i], spt[-i - 1] = spt[-i - 1], spt[i]
    print(driver_code_decrypt(spt, info))


def decrypt_grp(spt, info):
    amount_of_sym = int(input("По сколько символов было сгруппировано?"))
    exit_t = [info[i:i + amount_of_sym] for i in range(0, len(info), amount_of_sym)]
    for i in range(len(spt) // 2):
        spt[i], spt[-i - 1] = spt[-i - 1], spt[i]
    print(driver_code_decrypt(spt, exit_t))


def decrypt_word(spt, info):
    exit_t = info.split()
    for i in range(len(spt) // 2):
        spt[i], spt[-i - 1] = spt[-i - 1], spt[i]
    size_of_spt = len(spt)
    numeration = len(exit_t)
    code = ''
    for i in range(0, numeration, size_of_spt):
        new = [exit_t[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            code += str(new[size_of_spt - int(spt[j]) - 1])
            code += " "
    code = code.replace("0", "")
    print(code)



flag = True
if flag == True:
    Greetings()
    flag = False
