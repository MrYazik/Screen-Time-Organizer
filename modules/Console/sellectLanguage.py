print() # Отступ

def inputLanguage():
    

    with open('modules/Console/configs/language.txt', 'w+') as f:
        a = f.write("en")

    questionsForLanguage = input("Enter your language (en/ru): ")

    if (questionsForLanguage == "ru"):
        with open('modules/Console/configs/language.txt', 'w+') as f:
            a = f.write("ru")

        with open('configs/isActivatedOneSettings.txt', 'w+') as f:
            f.write("true")
        print() # Отступ
    elif (questionsForLanguage == "en"):
        with open('configs/isActivatedOneSettings.txt', 'w+') as f:
            f.write("true")

        print() # Отступ
    else:
        print("Have you entered something incorrectly")
        inputLanguage()

    return questionsForLanguage