from models import Constants
from mapping import training_mapper


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


def to_training_model(entity):
    result = training_mapper.map(entity)
    showed_up = entity[Constants.SHOW_UP]

    return result, showed_up





