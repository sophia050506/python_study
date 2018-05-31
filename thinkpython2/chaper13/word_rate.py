import string
def get_file(filename):
    hist = dict()
    file = open(filename)
    for line in file:
        get_line(line,hist)
    return hist

def get_line(line, hist):
    line = line.replace("-"," ")
    for word in line:
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = get_file('emma.txt')
print(hist, sum(hist.values()))
