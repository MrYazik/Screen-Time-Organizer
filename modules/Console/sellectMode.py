language = "" # Переменная для хранения языка

with open('modules/Console/configs/language.txt', 'r') as f:
    language = f.readline()

def inputQuestionsMode(): # Функция для запроса режима
    print() # Отступ

    # Сообщения 

    sellectModeValRussianInputMassage = "Выберите режим (если хотите узнать информацию о режимах введите: help) game/work: "
    sellectModeValEnglishInputMassage = "Select a mode (if you want to find out information about the modes, enter: help) game/work: "

    russianHelpMassage = "\nВот краткая информация о режимах: \n\n1. game - после завершения времени игры весь экран закрывается окном и в этом окне даются советы по разминке. \n2. work - после завершения времени работы в маленьком окне открываются совыты о разминке (по желанию их можно пропустить). \n\n*В обеих случаях в окне будет отображатся время до конца отдыха."
    englishHelpMassage = "\nHere is a brief information about the modes: \n\n1. game - after the end of the game time, the entire screen is closed by a window and warm-up tips are given in this window. \n2. work - after the end of the work time, warm-up notifications open in a small window (you can skip them if desired). \n\n*In both cases, the window will display the time until the end of the rest."

    # Переменные

    sellectModeVal = ""

    # Запрос выбора режима

    if (language == "ru"):
        sellectModeVal = input(sellectModeValRussianInputMassage)
    elif (language == "en"):
        sellectModeVal = input(sellectModeValEnglishInputMassage)

    # Обработка команд

    if (sellectModeVal == "help"):
        if (language == "ru"):
            print(russianHelpMassage)
        elif (language == "en"):
            print(englishHelpMassage)
        
        inputQuestionsMode() # Справшиваем режим заново

    elif (sellectModeVal == "game"):

        with open('modules/Console/configs/mode.txt', 'w+') as f:
            f.write("game")

    elif (sellectModeVal == "work"):

        with open('modules/Console/configs/mode.txt', 'w+') as f:
            f.write("game")

    else:
        print() # Отступ

        if (language == "ru"):
            print("Вы ввели что-либо неверно")
        elif (language == "en"):
            print("Have you entered something incorrectly")

        inputQuestionsMode() # Справшиваем режим заново        
