# Time Converter (24h to 12h)
''' function converts time from 24 h to 12 h '''
def time_converter(time):
    ''' function converts time from 24 h to 12 h '''
    hour = time.split(":")
    if time == '24:00' or time == '00:00':
        return '12:00 a.m.'
    elif int(hour[0]) < 12:
        return str(int(hour[0])) + ':' + hour[1] + ' a.m.'
    elif int(hour[0]) == 12:
        return time + ' p.m.'
    elif int(hour[0]) > 12:
        return (str(int(hour[0])-12) + ':' + hour[1] + ' p.m.')
    return "wrong time format"

if __name__ == '__main__':
    print("Example:")
    print(time_converter('09:00'))

'''
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''

# other solution

from datetime import datetime

def time_converter(time):
    d = datetime.strptime(time,"%H:%M")
    unit = " a.m." if int(d.strftime("%H")) < 12 else " p.m."
    return d.strftime("%-I:%M")+unit


# other solution

def time_converter(time):
    ampm = ' a.m.'
    time = time.split(':')
    if int(time[0]) >= 12 :
        ampm = ' p.m.'
    if int(time[0]) > 12 :
        time[0] = str(int(time[0])-12)
    elif int(time[0]) == 0 :
        time[0] = 12

    r = str(int(time[0])) + ':' + str(time[1]) + ampm
    return r