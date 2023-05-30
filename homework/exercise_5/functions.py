import json


def load_students():
    """Получаем список студентов из файла students.json"""
    with open('students.json', 'r', encoding='utf-8') as file:
        students = json.load(file)
        return students


def load_professions():
    """Получаем список профессий из файла professions.json"""
    with open('professions.json', 'r', encoding='utf-8') as file:
        professions = json.load(file)
        return professions


def get_student_by_pk(pk):
    """Выводим информацию о студенте по его номеру"""
    for st in load_students():
        if st['pk'] == int(pk):
            return st


def get_profession_by_title(title):
    """Выводим информацию о профессии по названию"""
    for prof in load_professions():
        if prof['title'] == title.capitalize():
            return prof


def check_fitness(student, profession):
    """Получаем информацию о студенте для введенной профессии"""
    user_info = {}
    student = set(get_student_by_pk(student)['skills'])
    profession = set(get_profession_by_title(profession)['skills'])
    user_info['has'] = profession.intersection(student)
    user_info['lacks'] = profession.difference(student)
    user_info['fitness_percent'] = int(len(user_info['has']) * 100 / len(profession))
    return user_info
