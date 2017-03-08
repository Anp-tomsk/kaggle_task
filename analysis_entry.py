from pymongo import MongoClient
from models.AppointmentInfo import to_training_model


client = MongoClient()
context = client.appointment_info

if __name__ == "__main__":
    collection = context.training_set
    for info in collection.find():
        print(type(info))
        training_model = to_training_model(info)
