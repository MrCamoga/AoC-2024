from functools import reduce

def readfile():
    with open("input.txt","r") as file:
        return (lambda v: [["."]*len(v[0])] + v + [["."]*len(v[0])])([["."]+[c for c in line.split()[0]]+["."] for line in file])

def part1(data):
    return sum((lambda a,b: a*b)(*(lambda f,x,y,c: f(f,x,y,c))(lambda f,x,y,c: (0,0) if data[y][x] == " " or data[y][x] == c.lower() else (0,1) if data[y][x] != c else data[y].__setitem__(x,c.lower()) or reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]), (f(f,x+dx,y+dy,c) for dx,dy in ((0,-1),(1,0),(0,1),(-1,0))), (1,0)), x,y,data[y][x])) for y in range(1,len(data)-1) for x in range(1,len(data[0])-1) if data[y][x] != ".")
    
def part2(data):
    return

if __name__  == "__main__":
    data = readfile()
    print(part1([[c for c in l] for l in data]))
    print(part2(data))
