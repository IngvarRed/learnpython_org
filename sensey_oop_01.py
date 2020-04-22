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
        return datetime.datetime.today().year - int(self.birth_date.split('-')[0])
    def get_fullname(self):
        return self.surname + ' ' + self.first_name



person1 = Person('bilinskyy', 'igor', '1971-12-26', 'ingvarr')

print(person1.nickname, person1.surname, person1.first_name, person1.birth_date)
print(person1.get_age())
print(person1.get_fullname())
