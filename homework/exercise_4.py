import random


def read_text():
    """Получаем слова из файла words.txt"""
    with open('words.txt', 'r', encoding="utf-8") as f:
        letters = [line.strip() for line in f]
        return letters


def add_the_result():
    """Добавляем имя пользователя и количество очков в файл history.txt"""
    with open('history.txt', 'a', encoding="utf-8") as f:
        return f.write(f"{user_input} {total_points}\n")


def get_max_result():
    """Получаем из файла history.txt количество попыток и максимальное количество баллов"""
    max_score = 0
    names_count = 0
    with open("history.txt", 'r', encoding="utf-8") as f:
        for line in f:
            names_count += 1
            parts = line.strip().split()
            score = int(parts[1])
            if score > max_score:
                max_score = score
    return f"\nВсего игр сыграно: {names_count} \nМаксимальный рекорд: {max_score}"


# Переменная с количеством баллов и с ответом пользователя
total_points = 0
user_input = input("Введите ваше имя\n")

# Выводим слова, перемешиваем их и просим пользователя отгадать, выводим ответ пользователю
for i in read_text():
    broken_word = list(i)
    random.shuffle(broken_word)
    jumbled_word = "".join(broken_word)
    print(f"\nУгадайте слово: {jumbled_word}")
    user_answer = input()
    if user_answer.lower() == i:
        print("Верно! Вы получаете 10 очков")
        total_points += 10
    else:
        print(f"Неверно! Верный ответ – {i}")

# Выводим результат
add_the_result()
print(get_max_result())





