'''
Домашнее задание к лекции 1.1 «Import. Module. Package»
Разработать структуру программы "Бухгалтерия".
main.py;
директория application:
-- salary.py;
-- директория db:
--- people.py;
main.py - основной модуль для запуска программы.
В модуле salary.py функция calculate_salary.
В модуле people.py функция get_employees.
Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
if __name__ == '__main__':
Сами функции реализовать не надо. Достаточно добавить туда какой-либо вывод.

Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
*4. Создать рядом с файлом main.py 
модуль dirty_main.py и импортировать все функции с 
помощью конструкции (необязательное задание)''

'''
import datetime
import time

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
TimeCreation = time.strftime("%H.%M.%S")

print("Local Date: ", TimeCreation + " " + DateCreation, "\n")

print("before import salary", "\n")

import salary

print("Module salary was imported", "\n")

print("before import people", "\n")

import people

print("Module people was imported", "\n")

print("Начато выполнение if __name__ == '__main__'", "\n")
if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
print("Закончено выполнение if __name__ == '__main__'")
