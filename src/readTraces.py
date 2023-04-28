import sys

class trace_t:
    def __init__(self, line):
        line = line.strip()
        if line[0] == '/':
            self.entry = False
            self.funcname = line[1:]
        else:
            self.entry = True
            self.funcname = line

    def __str__(self):
        if self.entry:
            return self.funcname
        else:
            return '/' + self.funcname

    def __repr__(self):
        return self.__str__()
        
def main(filename):
    traces = list()
    with open(filename, 'r') as f:
        for line in f:
            traces.append(trace_t(line))        

    print(traces)

if __name__ == "__main__":
    main(sys.argv[1])
