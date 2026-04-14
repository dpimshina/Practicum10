def seconds_from_start(date_str):
    date, time = date_str.split()

    month, day, year = map(int, date.split("/"))
    hour, minute, second = map(int, time.split(":"))

    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    total_days = sum(days_in_month[:month-1]) + (day - 1)

    total_seconds = total_days * 24 * 3600 + hour * 3600 + minute * 60 + second

    return total_seconds