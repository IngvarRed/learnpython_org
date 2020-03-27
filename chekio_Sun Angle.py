# Sun Angle
def sun_angle(time):
    '''Turns the sun between 6:00 AM and 6:00 PM, rounded to 2 decimal places'''
    l_time = time.split(':')
    hours = int(l_time[0])
    minutes = int(l_time[1])
    if hours < 6 or hours > 18:
        return "I don't see the sun!"
    elif hours == 18 and minutes > 0:
        return "I don't see the sun!"
    anggle = (hours-6) * 15 + minutes * 0.25
    return anggle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("17:01"))

'''
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


# Other solution

def sun_angle(time):
    # 180 degrees on 720 minutes (12 hours from 6 till 18 per 60 minutes in one)
    one_minute_angle = 180/(12*60)
    # get total minutes and normalize it in [0-720] range (substract first 6 hours per 60 minutes in one)
    minutes = int(time[0:2])*60 + int(time[3:5]) - 360
    # profit
    return round(minutes * one_minute_angle, 2) if 0 <= minutes <= 720 else "I don't see the sun!"