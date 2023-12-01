from email import header
from russian_names import RussianNames
import wonderwords
import csv
from phone_gen import PhoneNumber
import random
import string

params = {
    "number_doctors" : 2000,
    "number_diseases" : 1200,
    "number_drugs" : 4000,
    "number_cages" : 1500,
    "number_pets" : 5000
}

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def gen_cage():
    header = ['roomNumber', 'cageType', 'max_amount', 'amount']
    with open('./data/cages.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        
        for i in range(1, params['number_cages'] + 1):
            roomNumber = random.randint(0, 10)
            cageType = random.randint(0, 10)
            max_amount = random.randint(0, 6)
            amount = random.randint(0, max_amount)

            data = [roomNumber, cageType, max_amount, amount]
            writer.writerow(data)

def gen_doctor():
    header = ['nameDoc', 'surname', 'midname', 'phone', 'mail', 'birthD']
    with open('./data/doctors.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(params["number_doctors"]):
            name, midname, surname = RussianNames().get_person().split()

            number = PhoneNumber("Russia").get_number()

            mail = (random_char(7)+"@gmail.com")

            birth = '-'.join([str(random.randint(1970, 2002)), str(random.randint(1, 12)), str(random.randint(1, 28))])

            data = [name, surname, midname, number, mail, birth]
            writer.writerow(data)

def gen_disease():
    header = ['nameDis', 'symphtoms', 'reasons', 'deagnosis', 'dangerClassification']
    with open('./data/diseas.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(params["number_diseases"]):
            nameDis = wonderwords.RandomWord().word() + ' ' + wonderwords.RandomWord().word()

            symphtoms = wonderwords.RandomSentence().sentence()
            reasons = wonderwords.RandomSentence().sentence()
            deagnosis = wonderwords.RandomSentence().sentence()
            danger = random.randint(0, 100)

            data = [nameDis, symphtoms, reasons, deagnosis, danger]
            writer.writerow(data)

def gen_pTreatment():
    header = ['drugName', 'duration', 'contraindication', 'sideEffect']
    with open('./data/pTreatment.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(params["number_drugs"]):
            name = wonderwords.RandomWord().word() + " " + wonderwords.RandomWord().word()
            duration = random.randint(0, 60)
            contraindication = wonderwords.RandomSentence().sentence()
            sideEffect = wonderwords.RandomSentence().sentence()

            data = [name, duration, contraindication, sideEffect]
            writer.writerow(data)

def gen_pet():
    header = ['nameP', 'gender', 'weightP', 'birthDate', 'roomNumber']
    genders = ['m', 'f']
    with open('./data/pet.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(params["number_pets"]):
            nameP = wonderwords.RandomWord().word()
            gender = genders[random.randint(0,1)]
            weightP = random.randint(0, 40)
            birthD = '-'.join([str(random.randint(1970, 2002)), str(random.randint(1, 12)), str(random.randint(1, 28))])
            roomNumber = random.randint(1, params['number_cages'])

            data = [nameP, gender, weightP, birthD, roomNumber]
            writer.writerow(data)

def gen_dependenses(table_name, n, m):
    header = ['idn', 'idm']

    with open(table_name, 'w', newline='', encoding='WIN1252') as f:
        writer = csv.writer(f)
        writer.writerow(header)
    
        for i in range(n):
            idm = random.randint(1, m)
            data = [i + 1, idm]
            writer.writerow(data)

def main():
    pass
    # gen_doctor()
    # gen_disease()
    # gen_pTreatment()
    # gen_cage()
    # gen_pet()
    # gen_dependenses('./data/pTreatment_pet.csv', params['number_pets'], params['number_drugs'] - 1)
    # gen_dependenses('./data/disease_pet.csv', params['number_pets'], params['number_diseases'] - 1)
    # gen_dependenses('./data/doctor_pet.csv', params['number_pets'], params['number_doctors'] - 1)
    




if __name__ == "__main__":
    main()
