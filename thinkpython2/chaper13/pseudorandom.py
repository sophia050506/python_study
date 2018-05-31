import random
def test_random():
    for i in range(10):
        random.random() #返回0-1之间的浮点数，不包括1.0
        random.randint(5, 10)#返回5-10之间的整数，包括5和10
        #t = [1,2,3,4,5]
        t = ['hello','a','s']
        random.choice(t)#返回t中任意数字/字符
        print(random.choice(t))

def histogram(t):
    d = dict()
    count = 0
    for i in t:
        d[i] = d.get(i, 0) + 1
        count += 1
    return d

def choose_from_hist(t,count):
    for i in t:
        t[i] = t[i] / count
    return t

t = ['a','a','a','b','b','c']
print(choose_from_hist(histogram(t),len(t)))