class Questions:

    def __init__(self, text, complexity, correct_answer, asked=False, answer=None):
        self.text = text
        self.complexity = complexity
        self.correct_answer = correct_answer

        self.asked = asked
        self.answer = answer
        self.scored = self.complexity * 10
        self.total_score = 0

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.total_score)

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.correct_answer == self.answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        self.asked = True
        return f"Вопрос: {self.text}\nСложность: {self.complexity}/5"

    def build_feedback(self):
        """Возвращает : Ответ верный, получено __ баллов
        Возвращает : Ответ неверный, верный ответ __
        """
        if self.answer == self.correct_answer:
            self.total_score += int(self.scored)
            return f"Ответ верный, получено {self.scored} баллов\n"
        return f"Ответ неверный, верный ответ {self.correct_answer}\n"
