"""Игра: Угадай число.
Компьютер сам загадывает и сам угадывает число
"""
# Импортируем библиотеку numpy. Будем использовать ее для 
# генерации случайных чисел.
import numpy as np

# Ниже уже даны два простейших метода по угадыванию числа.

## Метод  первый: Случайное угадывание.

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

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

## Метод второй: Угадывание с коррекцией.

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

## Метод третий, мой метод: Расчет среднего значения.

def game_core_v3(number: int = 1) -> int:
    """Для сокращения кода создадим рекурсивную функцию 
        
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
        Сначала вычисляем число равное середине указанного диапазона, затем 
        сравниваем его с загаданным числом. Если среднее значение не равно 
        загаданному числу, значит определен новый диапазон поиска, которой в
        два раза меньше предыдущего. Затем вышеописанные действия повторяются
        до тех пор, пока расчетное число не совпадет с загаданным числом
        
        Аргументы рекурсивной функции - это границы поиска, которые сужаются
        с каждой последующей итерацией.
        
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

# Функция для оценки.

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

# Оценка работы алгоритмов.
## Определяем какой подход лучше

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