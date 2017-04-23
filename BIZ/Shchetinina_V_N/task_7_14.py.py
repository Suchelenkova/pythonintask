# Задача 7. Вариант 14.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Shchetinina V. N.
# 26.03.2017



import random 
 
talisman = random.choice(["Леопард","Зайка","Белый Мишка"]) 
 
x = 3 

y = 4 
 
print("Программа случайным образом загадала одного из трех официальных талисманов Олимпийских игр 2014!") 

print("Попробуйте отгадать за минимальное кол-во попыток!") 
 
print("\nМаксимальное кол-во очков: 12")

while x>0: 
	ask = input("Ваш ответ: ") 

	if ask == talisman: 
 
		print ("Правильно!") 
 
		break 
 
	else: 
 
		print ("Неверно!") 
 
		x = x - 1 

print ("Кол-во очков = ", x * y) 
 
input ("\nНажмите Enter, чтобы выйти")  
