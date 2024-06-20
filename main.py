# Подключаемые модули

from modules.Console.sellectLanguage import inputLanguage # Импортируем консольный модуль выбора языка

# Переменные

isActivatedOneSettings = "" # Переменная для записи был ли когда-то настроен язык программы

with open('configs/isActivatedOneSettings.txt', 'r') as f:
    isActivatedOneSettings = f.readline()

# Активация модулей

def OnSellectLanguage(): # Функция для вызова модуля по выбору языку
    if (isActivatedOneSettings == "false"):
        inputLanguage() # Активируем выбор языка    

OnSellectLanguage()