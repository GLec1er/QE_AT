def count_numbers():
    num = int(input("Введите количество циклопов: "))
    print('Введите их оптическую силу линзы:')
    dioptris = [int(input()) for _ in range(num)]
    dioptris.sort()

    number_ciklop = 0
    ans = 0

    while number_ciklop < num:
        if number_ciklop + 1 < num and dioptris[number_ciklop + 1] - dioptris[number_ciklop] <= 2:
            ans += 1
            number_ciklop += 2
        else:
            ans += 1
            number_ciklop += 1
    return ans


if __name__ == "__main__":
    result = count_numbers()
    print(f"Минимальное количество пар линз: {result}")
