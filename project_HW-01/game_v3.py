"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(number: int = 1) -> int:
    """Для написания более короткого кода создим рекурсивную функцию. 
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    
    def select(num_min=1, num_max=101):
        """Рекурсивная функция. 
        Ее цель - выполнять нужный повторяющийся порядок действий.
        Действия следующие:
        Сначала вычисляем среднее значение между максимум и минимум, затем 
        сравниваем его с нужным числом. Если среднее значение не равно нужному 
        числу, значит мы сузили "корридор" поиска в два раза. 
        Затем, в зависимости от результата, больше или меньше загаданное число,
        находим след. среднее значение и так далее, пока число не будет угадано.
        
        Аргументы функции - это границы поиска, которые сужаются с каждой 
        последующей итерацией.
        """        
        predict = (num_min + num_max) // 2 
        lst_tmp_up = [predict] 
        lst_tmp_down = [predict] 
        nonlocal count

        while number != predict: 
            count += 1
            if number > predict and number > (num_min + num_max) // 2:
                predict = (predict + num_max) // 2
                lst_tmp_up.append(predict)
            elif number < predict and number > (num_min + num_max) // 2:
                return select(lst_tmp_up[-2], lst_tmp_up[-1])
                        
            elif number < predict and number < (num_min + num_max) // 2:
                predict = (num_min + predict) // 2
                lst_tmp_down.append(predict)                
            elif number > predict and number < (num_min + num_max) // 2:
                return select(lst_tmp_down[-1], lst_tmp_down[-2])  
        
    select() 
    # Ваш код заканчивается здесь
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)

print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)