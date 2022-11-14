import json

list = []

with open('censorship.txt', encoding='utf-8') as file:
    for word in file:
        swear_word = word.lower().split('\n')[0]
        if swear_word: #Если это слово, а не пустая строка, будет True
            list = file.read().lower().split()

with open('censorsip.json', 'w', encoding='utf-8') as file:
    json.dump(list, file, indent = 4)