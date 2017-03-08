from models import Constants
from datetime import datetime


entity_mapping_info = {Constants.AGE: lambda value: int(value),
                       Constants.GENDER: lambda value: gender_from_str(value),
                       Constants.DATE_OF_REGISTRATION: lambda value: date_from_str(value),
                       Constants.APPOINTMENT_DATE: lambda value: date_from_str(value),
                       Constants.DAY_OF_WEEK: lambda value: value,
                       Constants.SHOW_UP: lambda value: show_up_from_str(value),
                       Constants.SMS_REMINDER: lambda value: value == "1",
                       Constants.TIME_OF_WAITING: lambda value: int(value),
                       Constants.DISEASES: lambda kwargs: get_diseases(kwargs)}


def date_from_str(value):
    return value[0:10]


def get_diseases(kwargs):
    diseases = []
    for key, value in kwargs.items():
        if key.lower() == Constants.DIABETES:
            if value == "1":
                diseases.append(Constants.DIABETES)
        if key.lower() == Constants.ALCOHOLISM:
            if value == "1":
                diseases.append(Constants.ALCOHOLISM)
        if key.lower() == Constants.HYPER_TENSION:
            if value == "1":
                diseases.append(Constants.HYPER_TENSION)
        if key.lower() == Constants.HANDICAP:
            if value == "1":
                diseases.append(Constants.HANDICAP)
        if key.lower() == Constants.SMOKES:
            if value == "1":
                diseases.append(Constants.SMOKES)
        if key.lower() == Constants.SCHOLARSHIP:
            if value == "1":
                diseases.append(Constants.SCHOLARSHIP)
        if key.lower() == Constants.TUBERCULOSIS:
            if value == "1":
                diseases.append(Constants.TUBERCULOSIS)

    return diseases


def gender_from_str(value):
    if value == "F" or value == "f":
        return "FEMALE"

    if value == "M" or value == "m":
        return "MALE"

    return "UNDEF"


def show_up_from_str(value):
    return value.lower() == "show-up"


def build_info(**kwargs):
    return to_entity(**kwargs)


def to_entity(**kwargs):
    entity = dict()
    for key in kwargs:
        if key in entity_mapping_info:
            value = kwargs[key]
            entity[key] = entity_mapping_info[key](value)

    return entity


def truncate_age(age):
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


def truncate_waiting_time(waiting_time):
    value = abs(int(waiting_time))

    if value < 5:
        return "less then five"

    if 5 <= value < 15:
        return "from 5 to 15"

    if 15 <= value < 30:
        return "from 15 to 30"

    return "more than 30"


def registration_before(appointment_date, registration_date):
    appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
    registration_date = datetime.strptime(registration_date, "%Y-%m-%d")

    value = (appointment_date - registration_date).days

    if value < 2:
        return "before one day"

    if 2 <= value < 7:
        return "from 2 to 7 days"

    if 7 <= value < 14:
        return "from 7 to 14 days"

    return "from 14 and upper"


def to_training_model(entity):
    age = entity[Constants.AGE]
    appointment_date = entity[Constants.APPOINTMENT_DATE]
    registration_date = entity[Constants.DATE_OF_REGISTRATION]
    gender = entity[Constants.GENDER]
    day_of_week = entity[Constants.DAY_OF_WEEK]
    sms_reminder = entity[Constants.SMS_REMINDER]
    time_of_waiting = entity[Constants.TIME_OF_WAITING]
    disease = entity[Constants.DISEASES]

    showed_up = entity[Constants.SHOW_UP]

    return {
        Constants.AGE: truncate_age(age),
        "registration_before": registration_before(appointment_date, registration_date),
        Constants.GENDER: gender,
        Constants.DAY_OF_WEEK: day_of_week,
        Constants.SMS_REMINDER: sms_reminder,
        "time_of_waiting": time_of_waiting,
        Constants.DISEASES: disease
    }, showed_up





