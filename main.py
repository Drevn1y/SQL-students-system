import sqlite3

# Подключение
con = sqlite3.connect('mydatabase.db')

# Переводчик
sql = con.cursor()

# Таблица
sql.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT, 
    age INTEGER, 
    grade TEXT
    )""")
# ======================================================================================================================
# # Ученики
# sql.execute("""INSERT INTO students (id, name, age, grade)
#     VALUES (101, 'Петя', 15, '4, 5, 3, 3, 2')
#     """)
# sql.execute("""INSERT INTO students (id, name, age, grade)
#     VALUES (102, 'Саша', 17, '3, 4, 5, 3, 3')
#     """)
# sql.execute("""INSERT INTO students (id, name, age, grade)
#     VALUES (103, 'Боря', 12, '2, 4, 5, 4, 3')
#     """)
# sql.execute("""INSERT INTO students (id, name, age, grade)
#     VALUES (104, 'Галя', 11, '5, 4, 5, 5, 2')
#     """)
# sql.execute("""INSERT INTO students (id, name, age, grade)
#     VALUES (105, 'Оля', 10, '5, 5, 5, 5, 4')
#     """)
# ======================================================================================================================

def info():
    list = sql.execute("SELECT * FROM students").fetchall()
    print(list)
def get_student_by_name():
    # Вывод
    choose = input('Введите имя ученика: ')
    students_list = sql.execute("SELECT grade FROM students WHERE name = ?", (choose,))
    print(choose, students_list.fetchone())

def update_student_grade():
    # Новая оценка
    info()
    student_name = input('Введите имя ученика: ')
    new_grade = input('Введите оценку: ')
    sql.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, student_name))
    con.commit()
    print('Оцека выставлено успешно!')

def delete_student():
    # Удалить студента
    info()
    student_name_del = input('Введите имя ученика: ')
    sql.execute("DELETE FROM students WHERE name = ?", (student_name_del,))
    con.commit()
    print('Удалено успешно!')

    info()

# Логика
while True:
    admin = int(input('1. Журнал\n2. Поставить новую оценку \n3. Удалить ученика\n4. Успеваемость учеников \n5. Выход \nВыполнить: '))

    if admin == 1:
        get_student_by_name()
    elif admin == 2:
        update_student_grade()
    elif admin == 3:
        delete_student()
    elif admin == 4:
        info()
    elif admin == 5:
        yn = input('If you want exit this program write Y else N:\t')
        if yn.title() == 'Y':
            break
        else:
            pass
    else:
        print('Увы, такой команды нет!')

    # Сохраняет
    con.commit()

# Закрытие
con.close()

