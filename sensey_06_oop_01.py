# Student class, which stores the student’s practical work

class Student:
    '''class, which stores the student’s practical work'''
    conf = {
        "lab_max": 10,  # the maximum number of points for one practical task
        "lab_num": 7  # number of practical tasks
    }
    def __init__(self, name, conf):
        self.name = name
        self.lab_max = conf['lab_max']
        self.lab_num = conf['lab_num']
        self.labs = [0] * self.lab_num

    def set_lab(self, score, number=None):
        '''saves points for practical work with the number'''
        if number is None and 0 in self.labs:
            number = self.labs.index(0)
        if number is None or number >= self.lab_num:
            return 'error'
        self.labs[number] = score if score <= self.lab_max else self.lab_max

    def average_score(self):
        '''returns a number rounded to tenths, the average score for practical tasks'''
        return round(sum(self.labs) / float(self.lab_num), 1)

