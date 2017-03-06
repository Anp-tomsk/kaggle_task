from models import Constants
from models.AppointmentInfo import build_info


def input_to_dict(line):
    args = line.split(',')
    return {
        Constants.AGE: args[0].strip(),
        Constants.GENDER: args[1].strip(),
        Constants.DATE_OF_REGISTRATION: args[2].strip(),
        Constants.APPOINTMENT_DATE: args[3].strip(),
        Constants.DAY_OF_WEEK: args[4].strip(),
        Constants.DISEASES : {
            Constants.DIABETES: args[6].strip(),
            Constants.ALCOHOLISM: args[7].strip(),
            Constants.HYPER_TENSION: args[8].strip(),
            Constants.HANDICAP: args[9].strip(),
            Constants.SMOKES: args[10].strip(),
            Constants.SCHOLARSHIP: args[11].strip(),
            Constants.TUBERCULOSIS: args[12].strip()
        },
        Constants.SMS_REMINDER: args[13].strip(),
        Constants.TIME_OF_WAITING: args[14].strip()
    }

if __name__ == "__main__":
    with open('data/medical_appointment.csv', 'r') as iFile:

        for i, line in enumerate(iFile.readlines()):
            if i == 0:
                continue

            if i < Constants.TRAINING_SET_RANGE:
                #To training dict
                args = input_to_dict(line)
                info = build_info(**args)

            if Constants.TRAINING_SET_RANGE <= i < Constants.VALIDATION_SET_RANGE:
                #To validation dict
                args = input_to_dict(line)
                info = build_info(**args)

            if i >= Constants.VALIDATION_SET_RANGE:
                #To hidden set
                args = input_to_dict(line)
                info = build_info(**args)
