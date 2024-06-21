# Подключаемые модули

from modules.Console.sellectLanguage import inputLanguage # Импортируем консольный модуль выбора языка
from modules.Console.enterFirstSettings import activatedFirstConfig # Импортируем консольный модуль активации первой настройки
from modules.Console.sellectMode import inputQuestionsMode # Испортируем модуль выбора режима

# Переменные

isActivatedOneSettings = "" # Переменная для записи был ли когда-то настроен язык программы

with open('configs/isActivatedOneSettings.txt', 'r') as f:
    isActivatedOneSettings = f.readline()

# Активация модулей

def ActivatedFirstSettings(): # Функция для вызова модуля по выбору языку
    if (isActivatedOneSettings == "false"):
        inputLanguage() # Активируем выбор языка   
        activatedFirstConfig() # Активируем модуль активации первой настройки

ActivatedFirstSettings()

# Запуск программы

inputQuestionsMode() # Запрашиваем режим

