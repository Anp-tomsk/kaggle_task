from mapping.dict_mapper import Mapper
from mapping.resolvers import *

training_mapper = Mapper()\
    .for_key("age", "age", age_resolver)\
    .for_key("time_of_waiting", "time_of_waiting", waiting_time_resolver)\
    .aggregate_keys(["appointment_date", "date_of_registration"], "registration_before", registration_time_resolver)