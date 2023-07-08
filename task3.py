# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01
history = []

def add_bank(cash: float):
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты: ", percent_add * bank)
    history.append(cash)

def take_bank(cash: float):
    global bank
    global count
    bank -= cash
    count += 1

    if cash*percent_take < 30:
        bank -= 30
        print("Cписаны проценты: ", 30)
    elif cash*percent_take > 600:
        bank -= 600
        print("Cписаны проценты: ", 600)
    else:
        bank -= cash * percent_take
        print("Списаны проценты: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты: ", percent_add * bank)
    history.append(-cash)

def tax_bank():
    global bank
    if bank > 5000000:
        bank = bank - bank * percent_tax
        print("Списан налог: ", bank * percent_tax)

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:

            return cash

def balance_bank():
    print("Баланс = ", bank)

def exit_bank():
    print("Выход из программы.")
    exit()


while True:
    action = input("ВЫБЕРИТЕ ДЕЙСТВИЕ:\n1 - Снять деньги\n2 - Пополнить\n3 - Баланс\n4 - История операций\n5 - Выйти\n")

    if action == '1':
        tax_bank()
        cash = check_bank()
        if cash < bank:
            take_bank(cash)
        else:
            print("Не хватает средств.")
        tax_bank()
        balance_bank()
    elif action == '2':
        add_bank(check_bank())
        tax_bank()
        balance_bank()
    elif action == '3':
        balance_bank()
    elif action == '4':
        print(history)
    else:
        exit_bank()