def final_price(price, has_card, is_holiday):
    discount = 0

    if price > 30000:
        discount += 10
    elif price > 20000:
        discount += 7
    elif price > 15000:
        discount += 5
    elif price > 5000:
        discount += 3

    if has_card:
        discount += 5

    if is_holiday:
        discount += 3

    if discount > 15:
        discount = 15

    final = price * (1 - discount / 100)
    return round(final, 2)