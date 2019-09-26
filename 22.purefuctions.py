#!/usr/bin/python3

# Demonstrating Pure Fuctions which don't modify the received parameters

print("Demonstrating Pure Functions")


class time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec


def addTime(t1, t2):
    '''pure function which adds two time objects and return a new time object'''
    sum = time(0, 0, 0)
    sum.sec = t1.sec + t1.sec
    sum.min = t1.min + t1.min
    sum.hr = t1.hr + t1.hr

    if(sum.sec > 60):
        sum.sec -= 60
        sum.min += 1

    if(sum.min > 60):
        sum.min -= 60
        sum.hr += 1

    return sum


if __name__ == "__main__":
    startTime = time(10, 34, 25)
    durationTime = time(2, 12, 41)
    endTime = addTime(startTime, durationTime)
    print("Movie Will end at: %d hr, %d min, %d sec" %
          (endTime.hr, endTime.min, endTime.sec))

# Demonstrating Modifier Fuctions which don't modify the received parameters
print("Demonstrating Modifier functions")


class time2:

    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
        print("Start Time is :"+str(self.hr), str(self.min), str(self.sec))


def incrementTime(startTime, addSeconds):
    startTime.hr = startTime.hr
    startTime.min = startTime.min
    startTime.sec = startTime.sec + addSeconds

    if(startTime.sec > 60):
        startTime.sec -= 60
        startTime.min += 1

    if(startTime.min > 60):
        startTime.min -= 60
        startTime.hr += 1

    return startTime


if __name__ == "__main__":
    startTime = time2(6, 50, 30)
    newTime = incrementTime(startTime, 30)
    print("New is: %d hr, %d min, %d sec" %
          (newTime.hr, newTime.min, newTime.sec))
