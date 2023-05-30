class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"{self.word}: {', '.join(self.subwords)}"

    def check_subword(self, word):
        """Проверяем введенное слово в списке допустимых подслов"""
        return word in self.subwords

    def count_subwords(self):
        """Считаем количество подслов"""
        return len(self.subwords)
