from functools import reduce

def get_yob(patient_dob):
    yob = []
    for date in patient_dob:
        yob.append(int(date.split('-')[2]))
    return yob

if __name__ == '__main__':
    patient_dob = ['13-06-1950', '04-10-2001', '26-09-2004']
    yob = get_yob(patient_dob)
    print(yob)

# map
# filter
# reduce
# lambda
# file.open()
# context for file in python
# nltk
# sci python
# jumpstart

# json.load
# json.dump
