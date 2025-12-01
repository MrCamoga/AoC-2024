import re

def readfile():
    with open("input.txt","r") as file:
        return [list(map(int,re.findall(r".*?(\d+).*?(\d+)",line)[0])) for line in file if line != "\n"]

def part1(data):
    return sum(map(lambda r: r[0][0]*3+r[1][0], filter(lambda r: r[0][1]==0 and r[1][1]==0 and 0<=r[0][0]<=100 and 0<=r[1][0]<=100, ((lambda z: (divmod(c[0]*b[1]-b[0]*c[1],z),divmod(a[0]*c[1]-c[0]*a[1],z)))(a[0]*b[1]-b[0]*a[1]) for a,b,c in zip(*[iter(data)]*3)))))

def part2(data):
    return sum(map(lambda r: r[0][0]*3+r[1][0], filter(lambda r: r[0][1]==0 and r[1][1]==0, ((lambda z: (divmod((c[0]+10000000000000)*b[1]-b[0]*(c[1]+10000000000000),z),divmod(a[0]*(c[1]+10000000000000)-(c[0]+10000000000000)*a[1],z)))(a[0]*b[1]-b[0]*a[1]) for a,b,c in zip(*[iter(data)]*3)))))

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
