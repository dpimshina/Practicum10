def format_date(date_str):
    try:
        date, time = date_str.split()

        month, day, year = date.split("/")
        hour, minute, second = time.split(":")

        month = int(month)
        day = int(day)
        hour = int(hour)

        if month < 1 or month > 12:
            print("Ошибка")
            return

        if day < 1 or day > 31:
            print("Ошибка")
            return

        period = "AM"
        if hour >= 12:
            period = "PM"
        if hour > 12:
            hour -= 12

        print(f"{day:02}.{month:02}.{year[2:]} {hour:02}:{minute}:{second} {period}")

    except:
        print("Ошибка формата")