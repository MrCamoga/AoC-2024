def readfile():
    with open("input.txt","r") as file:
        return [list(map(str.strip,line[0:7])) for line in zip(*[iter(file.readlines())]*8)]

def part1(data):
    return sum((lambda p: [all(i+j<=7 for i,j in zip(x,y)) for x in p[0] for y in p[1]])((lambda g,f,d,s,i: g(g,f,d,s,i))(lambda g,f,d,s,i: g(g,f,d,f(s,d[i]),i+1) if i < len(d) else s, lambda a,b: [a[0]+[b[1]],a[1]] if b[0]=="#" else [a[0],a[1]+[b[1]]], list(map(lambda key: (key[0][0],(lambda g,f,d,s,i: g(g,f,d,s,i))(lambda g,f,d,s,i: g(g,f,d,f(s,d[i]),i+1) if i < len(d) else s, lambda a,b: [a[i]+1 if x=="#" else a[i] for i,x in enumerate(b)], key, [0]*5, 0)),data)), [[],[]],0)))
def part2(data):
    return 

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
