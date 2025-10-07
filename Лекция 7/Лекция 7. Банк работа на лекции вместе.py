from datetime import datetime,date,time
class bankAccount:
  def __init__(self,id,balance):
    if(type(balance)==str):
      balance=int(balance)
    self.id=id
    self.balance=balance
    self.history=[]

  def deposit(self,money):
    if type(money)==int or money.isdigit():
      money=int(money)
      if(money>0):
        self.balance=self.balance+money
        print("Аккаунт пополнен")
        self.record("Полнение",money,datetime.now())
      else:
        print("Укажите положительное число")
    else:
      print("Пожалуйста, укажите число")

  def withdraw(self,money):
    if type(money)==int or money.isdigit():
      money=int(money)
      if(money>0 and self.balance>=money):
        self.balance=self.balance-money
        print("Сняли деньги с аккаунта")
        self.record("Снятие",money,datetime.now())
      else:
        print("Укажите корректную сумму, которую вы хотите снять с аккаунта")
    else:
      print("Пожалуйста, укажите число")

  def record(self,method,money,date):
    operation={
        "Операция":method,
        "Сумма":money,
        "Дата":date
    }
    self.history.append(operation)


  def getBalance(self):
    return self.balance

  def getHistory(self):
    print(self.history)
     

class savingsAccount(bankAccount):
  def __init__(self,id,balance,interestRate=0.1):
    super().__init__(id,balance)
    self.interestRate=interestRate

  def calculateInterest(self):
    newBalance=self.balance+self.balance*self.interestRate
    print("На счет пришли накопления по вкладу, новый балланс равен: ",newBalance)
    self.balance=newBalance
newAccount=bankAccount("1232151234",450)
newAccount.deposit(250)
newAccount.deposit("200")
newAccount.withdraw("598")
newAccount.getBalance()
newAccount.getHistory()
newSavingAccount=savingsAccount("1232151234",450,0.2)
newSavingAccount.calculateInterest()
