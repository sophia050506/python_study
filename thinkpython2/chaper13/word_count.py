import string
def get_word(file):
    d = dict()
    count = 0

    #获取每一行
    for f in file:
        word_list = f.split(" ")
        #取到单行的每个单词
        for word in word_list:
            table = str.maketrans(string.punctuation," " * len(string.punctuation))
            word = word.translate(table).strip()
            if word != "":
                d[word] = d.get(word,0) + 1
                count += 1
    print(count)
    print(d)

    #降序排列
    word_sort = sorted(d.items(), key=lambda d: d[1], reverse=True)
    print(word_sort)

    #取使用频率前10个
    for i in range(10):
        print(word_sort[i])  # ('the', 3850)
        print(word_sort[i][0]) #the

file = open("THE_SUBSTITUTE_MOLLONAIRE.txt","r",encoding="utf-8")
get_word(file)
