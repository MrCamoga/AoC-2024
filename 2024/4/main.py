def readfile():
    with open("input.txt","r") as file:
        d = ["   " + line.split()[0] + "   " for line in file]
        s = "".join([" "]*len(d[0]))
        return [s]*3+d+[s]*3

def part1(data):
    return sum(all(data[y+j*k][x+i*k]=="XMAS"[k] for k in range(4)) for i,j in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)) for x in range(3,len(data[0])-3) for y in range(3,len(data)-3))

def part2(data):
    return sum(all(any(all(data[y+j*l*(k-1)][x+i*l*(k-1)]=="MAS"[k] for k in (0,2)) for l in (-1,1)) for i,j in ((1,1),(1,-1))) for x in range(4,len(data[0])-4) for y in range(4,len(data)-4) if data[y][x]=="A")

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
