def add_time(start, duration, bool=False):

    initial_hour = initial_minutes = initial_m = start
    initial_m = initial_m[len(start)-2:]
    i = 0

    for x in start:
        if x == ":":
            initial_hour = int(initial_hour[:i])
            initial_minutes = int(initial_minutes[i + 1:i + 3])
            i = 0
            break
        i += 1

    add_hour = add_minute = duration

    for x in duration:
        if x == ":":
            add_hour = int(add_hour[:i])
            add_minute = int(add_minute[i + 1:])
            i = 0
            break
        i += 1

    final_hour = initial_hour + add_hour
    final_minutes = initial_minutes + add_minute

    if final_minutes > 59:
        final_minutes -= 60
        final_hour += 1

    day = 0
    noon = 0
    if initial_m == 'PM':
        noon = 1

    while final_hour > 11:
        final_hour -= 12
        if noon == 0:
            noon = 1
        else:
            noon = 0
            day += 1

    final_m = "AM"
    if noon == 1:
        final_m = "PM"

    if final_hour == 0:
        final_hour = 12

    final_hour = str(final_hour)
    if final_minutes < 10:
        final_minutes = "0" + str(final_minutes)
    else:
        final_minutes = str(final_minutes)

    days_of_the_week = 2 * ["Monday", "Tuesday", "Wednesday", "Thursday",
                            "Friday", "Saturday", "Sunday"]
    final_day_of_the_week = day
    while final_day_of_the_week > 7:
        final_day_of_the_week -= 7

    if day == 1:
        parenth = " (next day)"
    else:
        parenth = " ({} days later)"
        parenth = parenth.format(day)

    if bool:
        bool = bool.capitalize()
        final_bool = days_of_the_week[days_of_the_week.index(bool) +
                                      final_day_of_the_week]
        weekday = ", " + final_bool
    else:
        weekday = ""

    if day == 0:
        parenth = ""
    a = weekday + parenth
    result = final_hour + ":" + final_minutes + " " + final_m + a
    return result
