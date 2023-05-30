class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f"Пользователь {self.name} угадал {len(self.used_words)} слов: {', '.join(self.used_words)}"

    def get_used_words_count(self):
        """Получаем количество угаданных слов"""
        return len(self.used_words)

    def add_word(self, word):
        """Добавляем слово в угаданные слова"""
        self.used_words.append(word)

    def check_word_used(self, word):
        """Проверяем было ли уже использовано слово до этого"""
        return word in self.used_words
