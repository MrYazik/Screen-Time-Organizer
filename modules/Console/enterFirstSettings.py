# Скрипт для записи были ли бы запущены первые настройки

def activatedFirstConfig():
    with open('configs/isActivatedOneSettings.txt', 'w+') as f:
        f.write("true")