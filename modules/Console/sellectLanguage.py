print() # Отступ

def inputLanguage():
    

    with open('modules/Console/configs/language.txt', 'w+') as f:
        a = f.write("en")

    questionsForLanguage = input("Enter your language (en/ru): ")

    if (questionsForLanguage == "ru"):
        with open('modules/Console/configs/language.txt', 'w+') as f:
            a = f.write("ru")
        print() # Отступ
    elif (questionsForLanguage == "en"):

        print() # Отступ
    else:
        print("Have you entered something incorrectly")
        inputLanguage()

    return questionsForLanguage