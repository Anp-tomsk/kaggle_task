from models import Constants
from models.AppointmentInfo import build_info
from itertools import islice


def input_to_dict(line):
    args = line.split(',')
    return {
        Constants.AGE: args[0],
        Constants.GENDER: args[1],
        Constants.DATE_OF_REGISTRATION: args[2],
        Constants.APPOINTMENT_DATE: args[3],
        Constants.DAY_OF_WEEK: args[4],
        Constants.DISEASES : {
            Constants.DIABETES: args[6],
            Constants.ALCOHOLISM: args[7],
            Constants.HYPER_TENSION: args[8],
            Constants.HANDICAP: args[9],
            Constants.SMOKES: args[10],
            Constants.SCHOLARSHIP: args[11],
            Constants.TUBERCULOSIS: args[12]
        },
        Constants.SMS_REMINDER: args[13],
        Constants.TIME_OF_WAITING: args[14]
    }

if __name__ == "__main__":
    with open('data/medical_appointment.csv', 'r') as iFile:
            lines = list(islice(iFile, 2))[1:]
            for line in lines:
                args = input_to_dict(line)
                info = build_info(**args)
                print(info.age)
