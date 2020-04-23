# Implement a Person class that displays an entry in the contacts book
from datetime import datetime, date


class Person:
    '''Implement a Person class that displays an entry in the contacts book'''

    def __init__(self, surname, firstname, birthdate, nickname=None):
        self.surname = surname
        self.first_name = firstname
        self.nickname = surname if nickname is None else nickname
        date_format = "%Y-%m-%d"
        datetime_object = datetime.strptime(birthdate, date_format)
        self.birth_date = datetime_object.date()

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days / 365.25))

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.first_name)



person1 = Person('Bilinskyy', 'Vlad', '2001-04-24')

print(person1.nickname, person1.surname, person1.first_name, person1.birth_date)
print(person1.get_age())
print(person1.get_fullname())
