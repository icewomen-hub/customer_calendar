import pandas as pd


class DataProvider:

    course_plan = None
    time_slot_file = '../data/time_slot.csv'
    course_plan_file = '../data/course_plan.xlsx'
    trainer_file = '../data/trainer.csv'
    course_file = '../data/kurs.csv'
    auth_file = '../data/passwd.csv'
    # course_file = '../data/Kursplan.xlsx'

    weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']
    trainers = False
    courses = False
    time_slots = False

    def __init__(self):
        # self.course_plan = pd.read_excel(self.course_file)
        self.courses = pd.read_csv(self.course_file)
        self.trainers = pd.read_csv(self.trainer_file)
        self.time_slots = pd.read_csv(self.time_slot_file)
        self.roles = pd.read_csv(self.auth_file)

    def course_list(self):
        return self.courses

    def trainer_list(self):
        return self.trainers

    def weekday_list(self):
        return self.weekdays

    def time_slot_per_day(self, day):
        if day not in self.weekdays:
            self.stop(f'Ungültiger Wochentag:{day}')
        else:
            return self.time_slots[self.time_slots['wochentag'] == day]

    def time_slots_per_course(self, course):
        return self.time_slots[self.time_slots['kurs'] == course]

    def save(self, topic='course'):
        if topic == 'course':
            self.course.to_excel(self.course_file)

    def stop(self, msg):
        print('Fehler: ' + msg)
        exit()

