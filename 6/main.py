def readfile():
    with open("input.txt","r") as file:
        return [[s for s in line.split()[0]] for line in file]

def part1(data):
    dirs = ((0,-1),(1,0),(0,1),(-1,0))
    d = 0
    pos = [(j,i) for i,l in enumerate(data) for j,k in enumerate(l) if k == "^"][0]
    while True:
        while data[pos[1]+dirs[d][1]][pos[0]+dirs[d][0]] != "#":
            pos = [pos[0]+dirs[d][0],pos[1]+dirs[d][1]]
            data[pos[1]][pos[0]] = "X"
            if not (0 <= pos[1]+dirs[d][1] < len(data) and 0 <= pos[0]+dirs[d][0] < len(data[0])):
                break
        else:
            d = (d+1)&3
            continue
        return sum(c == "X" or c == "^" for line in data for c in line)   

def part2(data):
    dirs = ((0,-1),(1,0),(0,1),(-1,0))
    s = 0
    pos = [(j,i) for i,l in enumerate(data) for j,k in enumerate(l) if k == "^"][0]
    
    def loop(pos,d):
        for _ in range(len(data)*len(data[0])*4):
            while data[pos[1]+dirs[d][1]][pos[0]+dirs[d][0]] != "#":
                pos = [pos[0]+dirs[d][0],pos[1]+dirs[d][1]]
                if not (0 <= pos[1]+dirs[d][1] < len(data) and 0 <= pos[0]+dirs[d][0] < len(data[0])):
                    break
            else:
                d = (d+1)&3
                continue
            return False
        return True
            
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] in "^#":
                continue
            data[y][x] = "#"
            s += loop(pos[:],0)
            data[y][x] = "."
    return s

if __name__  == "__main__":
    data = readfile()
    print(part1([d[:] for d in data]))
    print(part2(data))
