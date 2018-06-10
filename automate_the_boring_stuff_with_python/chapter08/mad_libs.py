def mad_libse(filename):
    file = open(filename)
    line = file.read()
    print(line)
    word_list = []
    for word in line.split(" "):
        print(word)
        if word.isupper():
            word = input("Enter an %s" %(word.lower()))
        word_list.append(word)
    print(word_list)
    answer_file = open("answer.txt", "w")
    answer_file.write(" ".join(word_list))
    file.close()
    answer_file.close()

mad_libse('bacon.txt')