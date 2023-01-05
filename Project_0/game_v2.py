import numpy as np
def predict_number(number:int=1) -> int:
    count = 0
    number = np.random.randint(1, 101)
    print("Загадано число от 1 до 100")
    min = 0
    max = 100
    while True:
        predict_numer = round((min+max)/2)
        #predict = int(input())
        count += 1
        if number == predict_numer:
            break
        elif number > predict_numer:
            min = predict_numer
            print(f"Угадываемое число больше {predict_numer}")
            round((max + min) / 2)
        elif number < predict_numer:
            max = predict_numer
        print(f"Угадываемое число меньше {predict_numer}")
        round((max+min)/2)

    print(f"Вы угадали число {number} за {count} попыток.")
predict_number()