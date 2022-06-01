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
    flag_1 = True
    info = input("Введи текст сообщениия, которое необходимо защифровать: ")
    print("═" * 5, "Введите ключ, с помощью которого будет шифроваться текст. Например: '1 3 0 2' (вводить через пробелы)", "═" * 5)
    while flag_1 == True:
        spt_main = input("Ключ: ").split(" ")
        if len(spt_main) > 4:
            print('Длина ключа превышает допустимое значение.')
        else:
            flag_1 = False
            spt = []
            for e in spt_main:
                spt.append(int(e))
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
    flag_1 = True
    info = input("Введи текст сообщениия, которое необходимо расшифровать: ")
    while flag_1 == True:
        spt_main = input("Ключ, с помощью которого было зашифровано сообщение: ").split(" ")
        if len(spt_main) > 4:
            print('Длина ключа превышает допустимое значение.')
        else:
            flag_1 = False
            spt = []
            for e in spt_main:
                spt.append(int(e))
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
    size_of_spt = len(spt)
    numeration = len(info)
    structure = ''
    space = ''
    for i in range(0, numeration, size_of_spt):
        structure = [info[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            space += structure[spt.index(j)]
    return space


def drive_code_decrypt(spt, info):
    size_of_spt = len(spt)
    numeration = len(info)
    structure = ''
    space = ''
    for i in range(0, numeration, size_of_spt):
        structure = [info[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            space += structure[spt[j]]
    space = space.replace("0", "")
    return space


def letcrpt(spt, info):
    size_of_spt = len(spt)
    numeration = len(info)
    if numeration % size_of_spt != 0:
        for i in range(size_of_spt - (numeration % size_of_spt)):
            info += str("0")
    print(driver_code(spt, info))



def grpcrpt(spt, info):
    size_of_spt = len(spt)
    amount_of_group = int(input("На сколько символов разбить группу "))
    exit_t = [info[i:i+amount_of_group] for i in range(0, len(info), amount_of_group)]
    if len(exit_t[-1]) != amount_of_group:
        for i in range(amount_of_group - (len(exit_t[-1]) % amount_of_group)):
            exit_t[-1] += str("0")
    if len(exit_t) != size_of_spt:
        for i in range(size_of_spt - (len(exit_t) % size_of_spt)):
            exit_t.append("0" * amount_of_group)
    print(driver_code(spt, exit_t))


def wordcrpt(spt, info):
    size_of_spt = len(spt)
    exit_t = info.split(" ")
    if len(exit_t) != size_of_spt:
        for i in range(size_of_spt - (len(exit_t) % size_of_spt)):
            exit_t.append("0" * 5)
    numeration = len(exit_t)
    structure = ''
    space = ''
    for i in range(0, numeration, size_of_spt):
        structure = [exit_t[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            space += structure[spt.index(j)]
            space += " "
    print(space)


def decrypt_let(spt, info):
    print(drive_code_decrypt(spt, info))


def decrypt_grp(spt, info):
    amount_of_group = int(input("По сколько символов было сгруппировано? "))
    exit_t = [info[i:i + amount_of_group] for i in range(0, len(info), amount_of_group)]
    print(drive_code_decrypt(spt, exit_t))


def decrypt_word(spt, info):
    exit_t = info.split()
    size_of_spt = len(spt)
    numeration = len(exit_t)
    structure = ''
    space = ''
    for i in range(0, numeration, size_of_spt):
        structure = [exit_t[i + j] for j in range(size_of_spt)]
        for j in range(size_of_spt):
            space += structure[spt[j]]
            space += " "
    space = space.replace("0", "")
    print(space)


flag = True
if flag == True:
    Greetings()
    flag = False
