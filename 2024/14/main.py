import re
from functools import reduce

def readfile():
    with open("input.txt","r") as file:
        return [list(map(int,re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)",line)[0])) for line in file]

def part1(data,m=101,n=103):
    return reduce(lambda a,b: a*b, reduce(lambda a,b: tuple(a[i]+b[i] for i in range(4)), map(lambda p: (p[0]<m//2 and p[1]<n//2,p[0]>m//2 and p[1]<n//2,p[0]<m//2 and p[1]>n//2,p[0]>m//2 and p[1]>n//2), map(lambda p: ((p[0]+p[2]*100)%m,(p[1]+p[3]*100)%n), data)),(0,0,0,0)), 1)

def part2(data,m=101,n=103):
    return next((i for i in range(1,10000) if ((data:=list(map(lambda p: [(p[0]+p[2])%m,(p[1]+p[3])%n,p[2],p[3]],data))) and len(set(map(lambda p: (p[0],p[1]),data)))==len(data)))) * all(print("".join(map(str,reduce(lambda a,b: tuple(a[i]+b[i] for i in range(m)), map(lambda p: [0]*p[0]+[1]+[0]*(m-1-p[0]), filter(lambda p: p[1] == y,data)),[0]*m)))) or True for y in range(n))

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
    
