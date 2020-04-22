# Implement a Person class that displays an entry in the contacts book
import datetime


class Person:
    '''Implement a Person class that displays an entry in the contacts book'''

    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        if nickname:
            self.nickname = nickname
        else:
            self.nickname = surname
        print(self)
        self.birth_date = birth_date
    def get_age(self):
        today_d = datetime.datetime.today()
        age_day = self.birth_date.split('-')
        if today_d.month == int(age_day[1]) and today_d.day >= int(age_day[2]):
            return today_d.year - int(age_day[0])
        elif today_d.month > int(age_day[1]):
            return today_d.year - int(age_day[0])
        else:
            return today_d.year - int(age_day[0]) - 1
    def get_fullname(self):
        return self.surname + ' ' + self.first_name



person1 = Person('bilinskyy', 'igor', '1971-12-26', 'ingvarr')

print(person1.nickname, person1.surname, person1.first_name, person1.birth_date)
print(person1.get_age())
print(person1.get_fullname())
