def make_payment(P):
    limit = 1000
    min_payment = 20

    if P >= min_payment and P <= limit:
        print("Успех")
    else:
        print("Повторить попытку")