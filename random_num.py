import numpy as np
import time

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = 50
    corr = 50
    while number != predict:
        count+=1
        corr = int(round(corr/2+0.1, 0))
        # print(number, predict, corr)
        # time.sleep(10)
        if number > predict: 
            predict += corr
        elif number < predict: 
            predict -= corr
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)
