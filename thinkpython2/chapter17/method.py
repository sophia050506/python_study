class Time:

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

        #self.second = hour * 60 * 60 + minute * 60 + second

    def print_time(self):
        print("%.2d:%.2d:%.2d"%(self.hour,self.minute,self.second))

    def time_to_int(self):
        return self.hour * 60 * 60 + self.minute * 60 + self.second

    def int_to_time(self,second):
        time = Time()
        time.hour, minutes = divmod(second, 60 * 60)
        time.minute, time.second = divmod(minutes, 60)
        return time

    def increment(self,second):
        return self.int_to_time(self.time_to_int() + second)

    def is_after(self, after):
        print(after.time_to_int(),self.time_to_int())
        return after.time_to_int() > self.time_to_int()

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)

    def __str__(self):
        '''
        test_time = Time()
        print(test_time)
        self不赋值时会提示以下错误
        TypeError: __str__ returned non-string (type NoneType)
        '''
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)


    def __add__(self, other):
        if isinstance(other, Time):
            #return self.add_time(self, other)
            return self.int_to_time(self.time_to_int() + other.time_to_int())
        else:
            #return self.increment(self,other)
            return self.int_to_time(self.time_to_int() + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 < t2
start = Time()
start.hour = 1
start.minute = 0
start.second = 0
Time.print_time(start)
start.print_time()
print(start.time_to_int())
start.increment(3600).print_time()

end = Time()
end.hour = 0
end.minute = 0
end.second = 1
print(end.is_after(start))

test_time = Time(9, 45)
test_time.print_time()
print(test_time)

end_time = Time(1, 5)
print(test_time + end_time)
print(test_time + 15)
print(12 + test_time)

print("时间大小比较",Time(1,0) < Time(2))