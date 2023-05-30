import requests
import random
from basic_word import BasicWord

FILE_NAME = 'https://www.jsonkeeper.com/b/J3TP'


def load_random_word():
    """Получаем список слов и подслов и гегерируем рандомное слово"""
    response = requests.get(FILE_NAME)
    data = response.json()
    word_data = random.choice(data)
    return BasicWord(word_data["word"], word_data["subwords"])
