# 3) Создайте систему управления банковскими счетами, которая позволяет создавать, управлять и выполнять операции
# с банковскими счетами различных клиентов.
# Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента) и id
# (уникальный идентификатор клиента).
# Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты account_number (номер счета),
# balance (баланс счета) и client (объект типа Client, которому принадлежит счет).
# Класс также должен иметь методы deposit(amount) и withdraw(amount), которые позволяют пополнить или снять деньги со счета.
# Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является словарем,
# где ключами являются номера счетов, а значениями - объекты типа BankAccount. Класс также должен иметь методы
# create_account(client, initial_balance) для создания нового счета и get_account(account_number) для получения счета по его номеру.
# Добавьте в класс Bank методы для выполнения переводов между счетами (transfer(sender_account, receiver_account, amount))
# , а также для получения общего баланса клиента (get_total_balance(client)), который включает сумму денег на всех его счетах.
# Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или отсутствие счета при переводе.

class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class BankAccount:
    def __init__(self, account_number, balance, client):
        self.account_number = account_number
        self.balance = balance
        self.client = client

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств на счету.")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = 1
        while account_number in self.accounts:
            account_number += 1
        new_account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = new_account
        return new_account

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        return None

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account in self.accounts and receiver_account in self.accounts:
            if sender_account.balance >= amount:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
            else:
                print("Недостаточно средств на счете отправителя.")
        else:
            print("Указаны неверные номера счетов.")

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client == client:
                total_balance += account.balance
        return total_balance

# Создание банка и клиентов
bank = Bank()
client1 = Client("Иван Иванов", 1)
client2 = Client("Петр Петров", 2)

# Ввод данных от пользователя
initial_balance1 = int(input("Введите начальный баланс для счета клиента {}: ".format(client1.name)))
initial_balance2 = int(input("Введите начальный баланс для счета клиента {}: ".format(client2.name)))

# Создание банковских счетов
account1 = bank.create_account(client1, initial_balance1)
account2 = bank.create_account(client2, initial_balance2)

# Пополнение счета
amount_deposit = int(input("Введите сумму для пополнения счета клиента {}: ".format(client1.name)))
account1.deposit(amount_deposit)

# Снятие денег со счета
amount_withdraw = int(input("Введите сумму для снятия со счета клиента {}: ".format(client2.name)))
account2.withdraw(amount_withdraw)

# Перевод денег между счетами
amount_transfer = int(input("Введите сумму для перевода со счета клиента {} на счет клиента {}: ".format(client1.name, client2.name)))
bank.transfer(account1, account2, amount_transfer)

# Получение общего баланса клиента
total_balance = bank.get_total_balance(client1)

# Вывод информации
print(f"Баланс счета клиента {client1.name}: {account1.balance}")
print(f"Баланс счета клиента {client2.name}: {account2.balance}")
print(f"Общий баланс клиента {client1.name}: {total_balance}")


