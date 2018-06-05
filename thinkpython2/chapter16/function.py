class Time:
    pass

def print_time(time):
    print("%.2d:%.2d:%.2d"%(time.hours,time.minutes,time.second))


time = Time()
time.hours = 11
time.minutes = 11
time.second = 11
print_time(time)


def is_after(befortime,aftertime):
    if(befortime.hours > aftertime.hours) or (befortime.hours == aftertime.hours and befortime.minutes > aftertime.minutes)or (befortime.hours == aftertime.hours and befortime.minutes == aftertime.minutes and befortime.second > aftertime.second):
        return True
    else:
        return False

aftertime = Time()
aftertime = Time()
aftertime.hours = 5
aftertime.minutes = 11
aftertime.second = 56
print_time(aftertime)
#print(is_after(time,aftertime))

def add_time(befortime,aftertime):
    sum = Time()
    sum.hours = befortime.hours + aftertime.hours
    sum.minutes = befortime.minutes + aftertime.minutes
    sum.second = befortime.second + aftertime.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minutes += 1
    if sum.minutes >= 60:
        sum.minutes -= 60
        sum.hours += 1
    if sum.hours >= 24:
        sum.hours -= 24

    return sum

print_time(add_time(time,aftertime))

def time_to_int(time):
    return time.hours * 60 *60 + time.minutes * 60 + time.second

def int_to_time(second):
    time = Time()
    time.hours ,minutes = divmod(second, 60 * 60)
    time.minutes,time.second = divmod(minutes,60)
    return time


seconds = time_to_int(aftertime)
print(seconds)
print_time(int_to_time(seconds))



def valid_time(time):
    if time.hours < 0 or time.minutes < 0 or time.second < 0 :
        return False
    if time.minutes > 60 or time.second > 60 :
        return False
    return True

def add_time_fix(befortime,aftertime):
    assert valid_time(befortime) and valid_time(aftertime)
    return int_to_time(time_to_int(befortime) + time_to_int(aftertime))

print_time(add_time_fix(time,aftertime))

def mul_time(time,i):
    return int_to_time(time_to_int(time) * i)
