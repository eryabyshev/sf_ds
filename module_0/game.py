import numpy as np


def score_game(game_core_v1):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(100, size=1000)
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game(number, counter=0, all_number_var=None):
    if all_number_var is None:
        all_number_var = list(range(100))
    counter += 1
    mid = int(len(all_number_var) / 2)
    if all_number_var[mid] == number:
        return counter
    if number > all_number_var[mid]:
        return game(number, counter, all_number_var[mid + 1:])
    if number < all_number_var[mid]:
        return game(number, counter, all_number_var[:mid])


def main():
    score_game(game)


if __name__ == '__main__':
    main()
