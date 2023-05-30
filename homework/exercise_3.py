# Легкий уровень
words_easy = {"family": "семья", "hand": "рука", "people": "люди", "evening": "вечер", "minute": "минута"}

# Средний уровень
words_medium = {"believe": "верить", "feel": "чувствовать", "make": "делать", "open": "открывать", "think": "думать"}

# Сложный уровень
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме"
}

# Оценка пользователя
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

# Счетчик правильных ответов, все правильные ответы, все неправильные ответы, уровни ложности
# и словарь с уровнямисложностями
counter = 0
right_answers = []
incorrect_answers = []
words_values = ["легкий", "средний", "сложный"]
words = {"words_easy": "легкий", "words_medium": "средний", "words_hard": "сложный"}

# Вводим и проверяем есть ли такой уровень сложности в списке
while True:
    user_answer = input("Выберите уровень сложности. \nЛегкий, средний или сложный.\n")
    if user_answer.lower() not in words_values:
        print("Такого уровня нет.")
    else:
        break

# Выводим какой уровень выбрал пользователь, условие упражнения и просим нажать Enter
for one, two in words.items():
    if user_answer.lower() in words[one]:
        while input(f'Выбран уровень сложности {two}, мы предложим 5 слов, подберите перевод.\n'
                    f'Нажмите Enter.\n') != "":
            pass

# Вывод заданый при легком уровне сложности и подсчет правильных ответов
if user_answer.lower() == words["words_easy"]:
    for ing, rus in words_easy.items():
        print(f"{ing}, {len(rus)} букв, начинается на {rus[0]}...")
        answer = input()
        if answer.lower() == rus:
            print(f"Верно, {ing} — это {rus}\n")
            right_answers.append(ing)
            counter += 1
        else:
            print(f"Неверно. {ing} — это {rus}\n")
            incorrect_answers.append(ing)

# Вывод заданый при среднем уровне сложности и подсчет правильных ответов
elif user_answer.lower() == words["words_medium"]:
    for ing, rus in words_medium.items():
        print(f"{ing}, {len(rus)} букв, начинается на {rus[0]}...")
        answer = input()
        if answer.lower() == rus:
            print(f"Верно, {ing} — это {rus}\n")
            right_answers.append(ing)
            counter += 1
        else:
            print(f"Неверно. {ing} — это {rus}\n")
            incorrect_answers.append(ing)

# Вывод заданый при сложном уровне сложности и подсчет правильных ответов
elif user_answer.lower() == words["words_hard"]:
    for ing, rus in words_hard.items():
        print(f"{ing}, {len(rus)} букв, начинается на {rus[0]}...")
        answer = input()
        if answer.lower() == rus:
            print(f"Верно, {ing} — это {rus}\n")
            right_answers.append(ing)
            counter += 1
        else:
            print(f"Неверно. {ing} — это {rus}\n")
            incorrect_answers.append(ing)

# Вывод всех правильных ответов
if len(right_answers) == 0:
    pass
else:
    print("Правильно отвечены слова:")
    for x in right_answers:
        print(x)

# Вывод всех неправильных ответов
if len(incorrect_answers) == 0:
    pass
else:
    print("Неправильно отвечены слова:")
    for x in incorrect_answers:
        print(x)

# Вывод оценки
for number, grade in levels.items():
    if number == counter:
        print(grade)
