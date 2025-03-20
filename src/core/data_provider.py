import pandas as pd


class DataProvider:

    # Datenquellen:
    ## Bewegungsdaten
    course_plan_file = '../data/course_plan.xlsx'
    
    ## Stammdaten
    time_slot_file = '../data/time_slot.csv'
    trainer_file = '../data/trainer.csv'
    course_file = '../data/kurs.csv'
    auth_file = '../data/passwd.csv'
    weekday_file = '../data/wochentag.csv'
    
    weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']
    
    course_plan = None
    trainers = False
    courses = False
    time_slots = False
    
    current_topic = False

    valid_topics = ['courses', 'trainers','time_slots', 'roles', 'weekdays']
    
    def __init__(self, topic=False):
        
        if topic != False:
            self.current_topic = topic
            
        # self.course_plan = pd.read_excel(self.course_file)
        self.courses = pd.read_csv(self.course_file)
        self.trainers = pd.read_csv(self.trainer_file)
        self.time_slots = pd.read_csv(self.time_slot_file)
        self.roles = pd.read_csv(self.auth_file)
        self.weekdays = pd.read_csv(self.weekday_file)

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

    def save(self, topic='courses'):
        if topic == 'courses':
            self.course.to_excel(self.course_file)
        else:
            self.save_json(topic)
        # Save mee!



    def get_data(self, topic):
        self.topic = topic
        if topic == 'courses':
            return self.courses
        elif topic == 'trainers':
            return self.trainers
        elif topic == 'time_slots':
            return self.time_slots
        elif topic == 'roles':
            return self.roles
        elif topic == 'weekdays':
            return self.weekdays        
        
        
        
        return self.data

    def stop(self, msg):
        print('Fehler: ' + msg)
        exit()
