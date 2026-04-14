def special_numbers(A, B):
    if A > B:
        A, B = B, A

    allowed = {'1', '3', '4', '8', '9'}

    for num in range(A, B + 1):
        if all(digit in allowed for digit in str(num)):
            print(num)