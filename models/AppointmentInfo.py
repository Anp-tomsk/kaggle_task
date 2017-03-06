from enum import Enum
from models import Constants
import time


mapping_info = {Constants.AGE: lambda value: int(value),
                Constants.GENDER: lambda value: gender_from_str(value),
                Constants.DATE_OF_REGISTRATION: lambda value: date_from_str(value),
                Constants.APPOINTMENT_DATE: lambda value: date_from_str(value),
                Constants.DAY_OF_WEEK: lambda value: value,
                Constants.SHOW_UP: lambda value: show_up_from_str(value),
                Constants.SMS_REMINDER: lambda value: bool(value),
                Constants.TIME_OF_WAITING: lambda value: int(value),
                Constants.DISEASES: lambda kwargs: get_diseases(kwargs)}


def date_from_str(value):
    return time.strptime(value[0:10], "%Y-%m-%d")


def get_diseases(kwargs):
    diseases = []
    for key, value in kwargs.items():
        if key.lower() == Constants.DIABETES:
            if bool(value):
                diseases.append(Diseases.DIABETES)
        if key.lower() == Constants.ALCOHOLISM:
            if bool(value):
                diseases.append(Diseases.ALCOHOLISM)
        if key.lower() == Constants.HYPER_TENSION:
            if bool(value):
                diseases.append(Diseases.HYPER_TENSION)
        if key.lower() == Constants.HANDICAP:
            if bool(value):
                diseases.append(Diseases.HANDICAP)
        if key.lower() == Constants.SMOKES:
            if bool(value):
                diseases.append(Diseases.SMOKES)
        if key.lower() == Constants.SCHOLARSHIP:
            if bool(value):
                diseases.append(Diseases.SCHOLARSHIP)
        if key.lower() == Constants.TUBERCULOSIS:
            if bool(value):
                diseases.append(Diseases.TUBERCULOSIS)


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


def build_info(**kwargs):
    return AppointmentInfo(**kwargs)


class AppointmentInfo:
    def __init__(self, **kwargs):
        for key in kwargs:
            if key in mapping_info:
                value = kwargs[key]
                setattr(self, key, mapping_info[key](value))
