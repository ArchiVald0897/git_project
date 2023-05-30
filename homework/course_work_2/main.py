from players import Player
from utils import load_random_word


def declination():
    """склоняет слово 'слово' в зависимости от количества угаданных слов"""
    quantity = player.get_used_words_count()
    remainder = quantity % 100
    if remainder in range(11, 14):
        return f"{quantity} слов"
    elif remainder % 10 == 1:
        return f"{quantity} слово"
    elif remainder % 10 == 2 or remainder % 10 == 3 or remainder % 10 == 4:
        return f"{quantity} слова"
    else:
        return f"{quantity} слов"


player_name = input("Ввведите имя игрока: ")
player = Player(player_name)
print(f"Привет, {player_name}!")
word = load_random_word()
print(f'Составьте {word.count_subwords()} слов из слова "{word.word}"\nСлова должны состоять как минимум из 3 букв'
      f'\nЧтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')
print("Поехали!")

while player.get_used_words_count() < word.count_subwords():
    user_word = input("Введите Ваше слово: ")
    if len(user_word) < 3:
        print("Слово должно состоять как минимум из 3 букв!\n")
        continue
    if user_word.lower() == "stop" or user_word.lower() == "стоп":
        print(f"Игра завершена, вы угадали {declination()}")
        break
    if player.check_word_used(user_word.lower()):
        print("Уже использовано\n")
        continue
    if not word.check_subword(user_word.lower()):
        print("Неверно\n")
        continue
    player.add_word(user_word.lower())
    print("Верно\n")
