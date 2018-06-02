import os
def walk(dirname):
    for name in os.listdir(dirname):
        print(name)
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(os.path.abspath(path))
        else:
            walk(path)

#walk("/home/sophia/PycharmProjects/study")

def sed(s,f,infilename,outfilename):
    try:
        infile = open(infilename)
        outfile = open(outfilename,'w')
        for line in infile:
            line = line.replace(s,f)
            outfile.write(line)
        infile.close()
        outfile.close()
    except:
        print('读取文件异常')

#sed("2","3","/home/sophia/PycharmProjects/study/output.txt","out.txt")

def get_path_list(path):
    try:
        for name in os.listdir(path):
            abspath = os.path.join(path,name)
            #print(abspath)
            if os.path.isfile(abspath) and name.find(".txt") != -1:
                print(name,name.find(".txt"))
                print(abspath)
            else:
                get_path_list(abspath)
    except:
        print("路径不存在")

get_path_list("/home/sophia/PycharmProjects")