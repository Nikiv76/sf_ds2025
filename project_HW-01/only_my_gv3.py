"""Игра: Угадай число.
Компьютер сам загадывает и сам угадывает число
"""
# Импортируем библиотеку numpy. Будем использовать ее для 
# генерации случайных чисел.

import numpy as np

# Метод основан на рачете среднего значения

def game_core_v3(number: int = 1) -> int:
    """ Для сокращения кода создадим рекурсивную функцию.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1  
    
    def select(num_min=1, num_max=101):
        """ Рекурсивная функция. 
        Ее цель - выполнять нужный повторяющийся порядок действий.
        Действия следующие:
        Сначала вычисляем число равное середине указанного диапазона, затем 
        сравниваем его с загаданным числом. Если среднее значение не равно 
        загаданному числу, значит определен новый диапазон поиска, которой в
        два раза меньше предыдущего. Затем вышеописанные действия повторяются
        до тех пор, пока расчетное число не совпадет с загаданным числом
        
        Аргументы функции - это границы поиска, которые сужаются с каждой 
        последующей итерацией.
        
       Args:
            num_min (int, optional): Нижняя граница диапазона. Defaults to 1.
            num_max (int, optional): Верхняя граница диапазона. Defaults to 101.

        Returns:
            int: границы нового, уменьшенного диапазона.    
        """                
        predict = (num_min + num_max) // 2 
        lst_tmp_up = [predict] 
        lst_tmp_down = [predict] 
        nonlocal count

        while number != predict: 
            count += 1
            if number > predict and number > (num_min+num_max) // 2:
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
      
    return count 

# Функция для оценки.
def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)   фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))

    return score

# Оценка работы алгоритма

print(f"Ваш алгоритм угадывает число в среднем за: {score_game(game_core_v3)} попыток")   

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)