def readfromfile(path):
    with open(path,'r') as f:
        line = f.readline()
        while line != '':
            line = line.removesuffix('\n')
            yield line
            line = f.readline()

def getlines(path):
    with open(path,'r') as f:
        return f.read().split('\n')

def intializer(string,splitter=' '):
    return list(map(lambda x: int(x) ,string.split(splitter)))

def whiledigit(string:str,i):
    while i < len(string) and (string[i].isdigit() or string[i]=='-'):
        i += 1
    return i

def extractdigit(string,i):
    j = whiledigit(string,i)
    return int(string[i:j])