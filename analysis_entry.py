from pymongo import MongoClient
from models.AppointmentInfo import to_sklearn_model
from sklearn import tree
import pickle


client = MongoClient()
context = client.sklearn_appointment

if __name__ == "__main__":
    collection = context.training_set
    target_set = []
    feature_set = []
    for info in collection.find():
        target, features = to_sklearn_model(info)
        feature_set.append(features)
        target_set.append(target)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(feature_set, target_set)

    with open("tree.pcl", 'wb') as f:
        pickle.dump(clf, f)

