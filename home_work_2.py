# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

number_of_coins = int(input("Введите количество монет: "))

heads = 0
tails = 0
min_amount = 0
for i in range(number_of_coins):
    coins = random.randint(0, 1)
    print(coins)
    if coins == 0:
        heads += 1
    elif coins == 1:
        tails += 1
if heads < tails:
    min_amount = heads
elif tails < heads:
    min_amount = tails
elif tails == heads:
    print("Нет минимального значения")
print("Минимальное количество монет, которые нужно перевернуть", min_amount)