import functions

# Ввод номера студента и получаем имя студента по номеру
pk = input("Введите номер студента: \n")
name = functions.get_student_by_pk(pk)["full_name"]

# Выводим информацию о студенте
if functions.get_student_by_pk(pk):
    skills = functions.get_student_by_pk(pk)['skills']
    print(f"Студент: {name}\nЗнает: {', '.join(skills)}\n")
else:
    print('У нас нет такого студента')
    quit()

# Ввод профессии
title = input(f"Выберите специальность для оценки студента {name}\n")

# Выводим % пригодности для введенной профессии
# И выводим языки, которые студент знает и языки, которые студент не знает для введенной профессии
if functions.get_profession_by_title(title.capitalize()):
    if functions.check_fitness(pk, title)['fitness_percent'] <= 0:
        print(f"{name} не знает языков для этой профессии")
    else:
        print(f"Пригодность: {functions.check_fitness(pk, title)['fitness_percent']}% \n"
              f"{name} знает: {', '.join(functions.check_fitness(pk, title)['has'])}\n"
              f"{name} не знает: {', '.join(functions.check_fitness(pk, title)['lacks'])}")
else:
    print("У нас нет такой специальности")
    quit()
