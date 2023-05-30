# Всего баллов
total_points = 0
# Балы за попытки
point_for_attempts = 3
# Всего правельных ответов
right_answers = 0
# Всего попыток
total_attempts = 2

# Списки вопросов и правильных ответов
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# Приветствие
user_answer = input('Привет! \nПредлагаю проверить свои знания английского! \nНаберите "ready", чтобы начать! \n')

# Если пользователь вводит ready
if user_answer.lower() == "ready":
    # Вывод вопросов и запрос ответа
    for i in range(len(questions)):
        print(f"\nВопрос {i + 1}: \nНа выполнение задания Вам дается 3 попытки\nВедите пропущенное слово")
        print(questions[i], end='\n')
        # Условие, при котором пользователь вводит правильный ответ на вопрос
        answer = input()
        if answer.lower() == answers[i]:
            print('Ответ верный!')
            right_answers += 1
            total_points += point_for_attempts
        # Условие, при котором пользователь вводит неправильный ответ на вопрос
        # Водим расчет количества попыток
        else:
            while total_attempts > 0:
                answer = input(f"Неправильно. Осталось попыток: {total_attempts}, попробуйте еще раз!\n")
                if answer.lower() != answers[i]:
                    total_attempts -= 1
                    point_for_attempts -= 1
                elif answer.lower() == answers[i]:
                    print('Ответ верный!')
                    right_answers += 1
                    total_points += point_for_attempts
                    break
                else:
                    print(f"Попыток больше не осталось. Верный ответ: {answers[i]}")

    # Расчитывае процент правельных ответов
    percentage_of_completion = right_answers / len(questions) * 100

    # Выводим результат пользователю
    print(f'''\nВот и всё! \nВы набрали {total_points} баллов, ответив на {right_answers} вопроса из {len(questions)},
процент правильных ответов = {int(percentage_of_completion)}%''')

# Если вводит что-то другое
else:
    print("Кажется, вы не хотите играть. Очень жаль :(")
