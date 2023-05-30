import json
from modules import Questions

if __name__ == '__main__':

    QUESTIONS = 'questions.json'


    def right_answers(a):
        """Функция для внесения в список ответов"""
        return user_answers.append(a)


    def result_score(score, total_scored):
        """Функция для внесения баллов за ответы"""
        total_scored.append(score)
        return total_scored


    def load_question():
        """Получаем список вопросов из файла questions.json"""
        with open(QUESTIONS, encoding="utf-8") as file:
            return json.load(file)


    def declination():
        """склоняет слово вопрос в зависимости от количества правильно отвеченных вопросов"""
        quantity = user_answers.count(True)
        remainder = quantity % 100
        if remainder in range(11, 14):
            return f"{quantity} вопросов"
        elif remainder % 10 == 1:
            return f"{quantity} вопрос"
        elif remainder % 10 == 2 or remainder % 10 == 3 or remainder % 10 == 4:
            return f"{quantity} вопроса"
        else:
            return f"{quantity} питонов"


    # список ответов и баллов пользователя
    user_answers = []
    total_score = []

    # Запускаем игру, перебираем вопросы и обращаемся к списку
    print(input("Игра начинается!"))
    for questions in load_question():
        question = Questions(questions['q'], int(questions['d']), int(questions['a']))
        print(question.build_question())
        question.answer = int(input("Введите Ваш ответ\n"))
        right_answers(question.is_correct())
        print(question.build_feedback())
        result_score(question.get_points(), total_score)

    # Выводим результат игры
    print(f"\nВот и всё!\nОтвечено верно на {declination()} из {len(user_answers)}\n"
          f"Набранно: {sum(total_score)} баллов")
