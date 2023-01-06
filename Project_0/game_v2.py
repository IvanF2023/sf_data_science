"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict_number(number: int = 1) -> int: 
    """ Функция угадывает число 
    Args:
        number (int, optional): загаданное число. Defaults to 1.
    Returns:
        int: число попыток, потребоваашихся для отгадывания
    """    
    
    # Задаю границы интервала для поиска,
    # в дальнейшем будем делить его по пополам до результата
    min = 1
    max =  101

    count = 0
    while True:
        count += 1
        predict = (min + max) // 2 # Предположение
        if predict > number:
            max = predict
        elif predict < number:
            min = predict
        else:
            break
    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    pred_nums = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in pred_nums:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм {predict.__name__} угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_number)
