def count_letters(text):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"

    v_count = 0
    c_count = 0

    for char in text.lower():
        if char in vowels:
            v_count += 1
        elif char in consonants:
            c_count += 1

    print("Гласных:", v_count)
    print("Согласных:", c_count)
