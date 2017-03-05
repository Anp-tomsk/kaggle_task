from enum import Enum
import time

mapping_info = {"age": lambda value: int(value),
                "gender": lambda value: gender_from_str(value),
                "date_of_registration": lambda value: time.strptime(value, "%Y-%m-%d"),
                "appointment_date": lambda value: time.strptime(value, "%Y-%m-%d"),
                "day_of_week": lambda value: value,
                "show_up": lambda value: show_up_from_str(value),
                "sms_reminder": lambda value: bool(value),
                "time_of_waiting": lambda value: int(value),
                "diseases": lambda **kwargs: get_diseases(kwargs)}


def get_diseases(**kwargs):
    for key, value in kwargs:
        pass


def gender_from_str(value):
    if value == "F" or value == "f":
        return Gender.FEMALE

    if value == "M" or value == "m":
        return Gender.MALE

    return Gender.UNDEF


def show_up_from_str(value):
    return value.lower() == "show-up"


class Gender(Enum):
    MALE = 1,
    FEMALE = 2,
    UNDEF = 3


class Diseases(Enum):
    DIABETES = 1,
    ALCOHOLISM = 2,
    HYPER_TENSION = 3,
    HANDICAP = 4,
    SMOKES = 5,
    SCHOLARSHIP = 6,
    TUBERCULOSIS = 7


class AppointmentInfo:
    def __init__(self, **kwargs):
        for key, value in kwargs:
            if key in mapping_info:
                value = kwargs[key]
                setattr(self, key, mapping_info[key](value))
