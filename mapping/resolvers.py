from datetime import datetime


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]


def default_resolver(value):
    return value


def age_resolver(age):
    value = int(age)

    if value < 5:
        return 1

    if 5 <= value < 11:
        return 2

    if 11 <= value < 16:
        return 3

    if 16 <= value < 20:
        return 4

    if 20 <= value < 30:
        return 5

    if 30 <= value < 60:
        return 6

    return 7


def waiting_time_resolver(waiting_time):
    value = abs(int(waiting_time))

    if value < 5:
        return 0

    if 5 <= value < 15:
        return 1

    if 15 <= value < 30:
        return 2

    return 3


def day_of_week_resolver(day_of_week):
    return days_of_week.index(day_of_week)


def registration_time_resolver(appointment_date, date_of_registration):
    appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
    registration_date = datetime.strptime(date_of_registration, "%Y-%m-%d")

    value = (appointment_date - registration_date).days

    if value < 2:
        return 0

    if 2 <= value < 7:
        return 1

    if 7 <= value < 14:
        return 2

    return 3


def diseases_resolver(diseases):
    result = []
    for key, _ in diseases.items():
        result.append(key)
    return result


