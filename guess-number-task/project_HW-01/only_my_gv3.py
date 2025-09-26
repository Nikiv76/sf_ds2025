import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Для написания более короткого кода создим рекурсивную функцию.
    
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
    # Ваш код заканчивается здесь
    
def score_game(game_core_v3) -> int:
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
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
score_game(game_core_v3)