# всего баллов
total_points = 0
# всего правельных ответов
right_answers = 0

# Получаем имя пользователя и приветсвуем его
user_name = input("Привет! Предлагаю проверить свои знания английского! \nНапиши, как тебя зовут.\n")
print(f"Привет, {user_name}, начинаем тренировку!\n")

# переходим к вопросам
# в случае правильного ответа увеличиваем баллы и количество правельных ответов
print("Вопрос 1:")
print("My name ___ Vova.")
answer_one = input("Ведите пропущенное слово ")

if answer_one.lower() == "is":
    print("Ответ верный \nВы получаете 10 баллов!\n")
    total_points += 10
    right_answers += 1
else:
    print("Неправильно. \nПравильный ответ: is\n")

print("Вопрос 2:")
print("I ___ a coder.")
answer_two = input("Ведите пропущенное слово ")

if answer_two.lower() == "am":
    print("Ответ верный \nВы получаете 10 баллов!\n")
    total_points += 10
    right_answers += 1
else:
    print("Неправильно. \nПравильный ответ: am\n")

print("Вопрос 3:")
print("I live ___ Moscow.")
answer_three = input("Ведите пропущенное слово ")

if answer_three.lower() == "in":
    print("Ответ верный \nВы получаете 10 баллов!\n")
    total_points += 10
    right_answers += 1
else:
    print("Неправильно. \nПравильный ответ: am\n")

# расчитывае процент правельных ответов
percentage_of_completion = right_answers/3*100

# выводим результат пользователю
print(f"Вот и всё, {user_name}! \nВы ответили на {right_answers} вопросов из 3 верно.")
print(f"Вы заработали {total_points} баллов. \nЭто {int(percentage_of_completion)} процентов.")
