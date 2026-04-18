def format_date(date_str):
    """Преобразует дату из формата MM/DD/YYYY HH:MM:SS в DD.MM.YY HH:SS AM/PM."""
    try:
        date, time = date_str.split()
        month, day, year = date.split("/")
        hour, minute, second = time.split(":")

        month = int(month)
        day = int(day)
        hour = int(hour)

        if not (1 <= month <= 12):
            print("Ошибка")
            return

        if not (1 <= day <= 31):
            print("Ошибка")
            return

        period = "AM"
        if hour >= 12:
            period = "PM"
        if hour > 12:
            hour -= 12

        print(f"{day:02}.{month:02}.{year[2:]} {hour:02}:{minute:02}:{second:02} {period}")

    except (ValueError):
        print("Ошибка формата")
