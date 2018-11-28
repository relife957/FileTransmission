

def read():
    filepath = "/home/wangyi/文档/"
    filename = "data.dat"
    f = open(filepath+filename,'r')

    data = f.readlines()

    f.close()
    return data