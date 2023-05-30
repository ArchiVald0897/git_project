# Импортируем модуль рандома
import random


def get_random_word():
    """Получает случайное слово из списка"""
    words = ["code", "bit", "list", "soul", "next", "family", "believe", "feel", "make", "people", "minute", "SOS"]
    word_random = random.choice(words)
    return word_random


def morse_encode():
    """Переводит случайное слово на английском языке в последовательности точек и тирe"""
    morse_word = ""
    morse_code = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    for letter in random_word:
        morse_word += morse_code[letter.lower()] + " "
    return morse_word


def print_statistics():
    """Подсчитываем статистику выполненых заданий"""
    return f"Всего задачек: {len(answers)} \nОтвечено верно: {answers.count(True)} \n" \
           f"Отвечено неверно: {answers.count(False)}"


# Счетчик номера задания и ответы пользователя
number_word = 1
answers = []

# Прописываем условия выполнения задания и просим нажать Enter для продолжения
while input('Сегодня мы потренируемся расшифровывать азбуку Морзе\n'
            'Нажмите Enter и начнем\n') != "":
    pass

# Выводим задания и принимаем ответы пользователя
while number_word <= 5:
    random_word = get_random_word()
    print("Слово " + str(number_word) + ": " + (morse_encode()))
    user_input = input("Введите перевод этого слова\n")
    if user_input.lower() == random_word.lower():
        print("Верно, " + str(random_word) + "!\n")
        answers.append(True)
    else:
        print("Неверно, правильный ответ " + str(random_word) + "!\n")
        answers.append(False)
    number_word += 1

# Выводим статистику
print(print_statistics())
