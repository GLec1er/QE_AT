def calculate_change(price, money):
    """
    Рассчитывает сдачу и возвращает её в виде строки.
    """
    money_bank = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]

    if money < price:
        return 'У вас не хватает денежных средств'

    diff = money - price
    if diff == 0:
        return 'Товар полностью оплачен'

    change_list = []
    for i in money_bank:
        cnt = diff // i
        if cnt > 0:
            diff -= cnt * i
            change_list.append(f"{i} руб: {cnt} шт.")
    change_str = ", ".join(change_list)
    return f'{change_str}'


def main():
    try:
        price = int(input("Введите стоимость товара: "))
        money = int(input("Введите сумму, которую вы вносите: "))

        result = calculate_change(price, money)
        print(result)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()
