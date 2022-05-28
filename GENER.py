def Greetings():
    print("═" * 45)
    print("Алоха! Я - разум по шифрованию текстов.\nВ мой перечень услуг входит:")
    print("1 - Шифровка. \n2 - Расшифровка.")
    start = int(input("Выбери нужную тебе функцию: "))
    if start == 1:
        crypt()
    else:
        decrypt()

while(True):
    Greetings()
    text = 0

def crypt():

def decrypt():