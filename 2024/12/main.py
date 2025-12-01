from functools import reduce
from itertools import groupby
from operator import itemgetter

def readfile():
    with open("input.txt","r") as file:
        return (lambda v: [["."]*len(v[0])] + v + [["."]*len(v[0])])([["."]+[c for c in line.split()[0]]+["."] for line in file])

def part1(data):
    return sum((lambda a,b: a*b)(*(lambda f,x,y,c: f(f,x,y,c))(lambda f,x,y,c: (0,0) if data[y][x] == " " or data[y][x] == c.lower() else (0,1) if data[y][x] != c else data[y].__setitem__(x,c.lower()) or reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]), (f(f,x+dx,y+dy,c) for dx,dy in ((0,-1),(1,0),(0,1),(-1,0))), (1,0)), x,y,data[y][x])) for y in range(1,len(data)-1) for x in range(1,len(data[0])-1) if data[y][x] != ".")

def part2(data):
    return sum(map(lambda r: r[0]*sum(sum(map(lambda p: sum(1 for _,j in groupby(p) if next(j)), map(lambda p: [i in p for i in range(max(p)+1)], l))) for l in [[list(map(itemgetter(i&1),v)) for k,v in groupby(sorted(r[1+i],key=itemgetter((i&1)^1)),itemgetter((i&1)^1))] for i in range(4)]),list((lambda f,x,y,c,d: f(f,x,y,c,d))(lambda f,x,y,c,d: (0,*[set()for _ in range(4)]) if data[y][x] == " " or data[y][x] == c.lower() else (0,*[set()if i!=d else set([(x,y)])for i in range(4)]) if data[y][x] != c else data[y].__setitem__(x,c.lower()) or reduce(lambda a,b: (a[0]+b[0],*(a[i]|b[i] for i in range(1,5))), (f(f,x+dx,y+dy,c,d) for d,(dx,dy) in enumerate(((0,-1),(1,0),(0,1),(-1,0)))), (1,set(),set(),set(),set())), x,y,data[y][x],0) for y in range(1,len(data)-1) for x in range(1,len(data[0])-1) if data[y][x] != ".")))
    

if __name__  == "__main__":
    data = readfile()
    print(part1([[c for c in l] for l in data]))
    print(part2(data))
