def readfile():
    with open("input.txt","r") as file:
        return (lambda v: [[-1]*len(v[0])]+v+[[-1]*len(v[0])])([[-1] + list(map(int,line.split()[0])) + [-1] for line in file])
    
def part1(data):
    return sum(len((lambda f,x,y,v: f(f,x,y,v))(lambda f,x,y,v: set() if data[y][x]!=v else set([(x,y)]) if v==9 else {e for s in (f(f,x+i[0],y+i[1],v+1) for i in ((-1,0),(0,-1),(1,0),(0,1))) for e in s},x,y,0)) for x,y in [(i,j) for j in range(len(data)) for i in range(len(data[0])) if data[j][i] == 0])

def part2(data):
    return sum((lambda f,x,y,v: f(f,x,y,v))(lambda f,x,y,v: 0 if data[y][x]!=v else 1 if v==9 else sum(f(f,x+i[0],y+i[1],v+1) for i in ((-1,0),(0,-1),(1,0),(0,1))),x,y,0) for x,y in [(i,j) for j in range(len(data)) for i in range(len(data[0])) if data[j][i] == 0])

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
