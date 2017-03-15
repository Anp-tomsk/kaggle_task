from mapping.dict_mapper import Mapper, DictToArrMapper
from mapping.resolvers import *

training_mapper = Mapper()\
    .for_key("age", "age", age_resolver)\
    .for_key("time_of_waiting", "time_of_waiting", waiting_time_resolver)\
    .ignore_key("show_up")\
    .ignore_key("_id")\
    .ignore_key("diseases")\
    .aggregate_keys(["appointment_date", "date_of_registration"], "registration_before", registration_time_resolver)

arr_mapper = DictToArrMapper()\
    .for_key("age", age_resolver)\
    .for_key("time_of_waiting", waiting_time_resolver)\
    .for_key("gender")\
    .for_key("day_of_week")\
    .ignore_key("show_up")\
    .ignore_key("_id")\
    .for_key(["appointment_date", "date_of_registration"], registration_time_resolver)