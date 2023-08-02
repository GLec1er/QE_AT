def sieve_of_eratosthenes(limit):
    """
    Реализация алгоритма Решето Эратосфена для нахождения простых чисел до заданного значения.
    """
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i in range(limit + 1) if primes[i]]


def sum_simple_digits(num):
    """
    Находит сумму всех простых чисел от 2 до заданного числа num.
    """
    if num <= 1:
        return 0

    primes = sieve_of_eratosthenes(num)
    return sum(primes)


def main():
    """
    Основная функция программы, которая запрашивает у пользователя положительное число
    и выводит сумму всех простых чисел от 2 до этого числа.
    """
    while True:
        try:
            num = int(input("Введите положительное число: "))
            if num < 0:
                print("Пожалуйста, введите положительное число.")
            elif num == 0 or num == 1:
                print(f"Сумма всех простых чисел равна 0.")
                break
            else:
                result = sum_simple_digits(num)
                print(f"Сумма всех простых чисел от 2 до {num} равна {result}.")
                break
        except ValueError:
            print("Пожалуйста, введите целое положительное число.")


if __name__ == "__main__":
    main()
