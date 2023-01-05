"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0
min = 0
max = 100
while True:
   
    predict_number = int(input("Введите число: "))
    count+=1
    if predict_number == number:
        break

    elif predict_number < number:
        min = predict_number
        print(f"Число должно быть больше {predict_number}")
        print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max + min) / 2)}')
    
    elif number < predict_number:
        max = predict_number
        print(f"Число должно быть меньше {predict_number}")
        print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max + min) / 2)}')
print(f"Вы угадали число! Это число {number}, за {count} попыток")
    
    