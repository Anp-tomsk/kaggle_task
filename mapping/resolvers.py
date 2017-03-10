from datetime import datetime


def default_resolver(value):
    return value


def age_resolver(age):
    value = int(age)

    if value < 5:
        return "Before 5"

    if 5 <= value < 11:
        return "From 5 to 11"

    if 11 <= value < 16:
        return "From 11 to 16"

    if 16 <= value < 20:
        return "From 16 to 20"

    if 20 <= value < 30:
        return "From 20 to 30"

    if 30 <= value < 60:
        return "From 30 to 60"

    return "From 60 and older"


def waiting_time_resolver(waiting_time):
    value = abs(int(waiting_time))

    if value < 5:
        return "less then five"

    if 5 <= value < 15:
        return "from 5 to 15"

    if 15 <= value < 30:
        return "from 15 to 30"

    return "more than 30"


def registration_time_resolver(appointment_date, date_of_registration):
    appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
    registration_date = datetime.strptime(date_of_registration, "%Y-%m-%d")

    value = (appointment_date - registration_date).days

    if value < 2:
        return "before one day"

    if 2 <= value < 7:
        return "from 2 to 7 days"

    if 7 <= value < 14:
        return "from 7 to 14 days"

    return "from 14 and upper"


