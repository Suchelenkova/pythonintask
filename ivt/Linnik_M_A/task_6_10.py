# Задача 6. Вариант 10.
#Создайте игру, в которой компьютер загадывает название одной из трех стран, входящих в военно-политический блок "Тройственный союз", а игрок должен его угадать.

# Linnik A. M.
# 04.04.2017

import random

answer = input('Я загадал одну страну из "Тройственного союза".'
      +'\nПопробуй отгадать:'
      +'\n1 - Германия, 2 - Астро-венгрия, 3 - Италия'
      +'\nТвой ответ: ')

n = random.randint(1, 3)
if(int(answer) == n):
    result = '\nТы угадал'
else:
    result = '\nТы не угадал'
print(result)
input('\n\nНажмите Enter для выхода.')