import string
import random
'''
读文件
'''
def get_file(filename):
    hist = dict()
    file = open(filename)
    for line in file:
        get_line(line,hist)
    return hist

'''
打印所有使用到的单词及使用次数
strip()可以去首尾，中间无法去除
'''
def get_line(line, hist):
    line = line.replace("-"," ")
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

'''
排序
key排序 sorted(e.items(), key=lambda e: e[0])
value排序 sorted(e.items(), key=lambda e: e[1])
倒序：reverse=True
'''
def most_common(hist):
    t = sorted(hist.items(), key=lambda e: e[1], reverse=True)
    print(t)
    return t

def print_most_common(hist,num=10):
    t = most_common(hist)
    for word,freq in t[:num]:
        print(word,freq)

'''
在d1不在d2中的key
'''
def subtract(d1,d2):
    d = dict()
    for key in d1:
        if key not in d2:
            d[key] = None
    return d
#字典
#hist = get_file('emma.txt') #单词总数: 162742 ;不同的单词数： 7460
#print("单词总数:",sum(hist.values()),";不同的单词数：",len(hist))
#print_most_common(hist,20)
'''
word = get_file("words.txt")
diff = subtract(hist,word)
for word in diff.keys():
    print(word, end=' ')
'''
#集合set
def get_diff_word(filename):
    hist = set()
    file = open(filename)
    for line in file:
        line = line.replace("-", " ")
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            hist.add(word)
    return hist
'''
s1 = get_diff_word("emma.txt")
s2 = get_diff_word("words.txt")
print(s1 - s2)
'''

def random_word(h):
    t = []
    for word , freq in h.items():
        #print(word,freq,[word] * freq)
        t.extend([word] * freq)
    return random.choice(t)

h = get_file("emma.txt")
print(random_word(h))