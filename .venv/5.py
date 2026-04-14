def phone_card():
    price = int(input("Введите стоимость карты: "))

    if price == 5 or price == 10:
        return price
    elif price == 25:
        return price + 3
    elif price == 50:
        return price + 8
    elif price == 100:
        return price + 20
    else:
        print("Неверное значение")
        return None