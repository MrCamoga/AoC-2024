def readfile():
    with open("input.txt","r") as file:
        return [line.split()[0] for line in file]

def part1(data):
    return len(set(filter(lambda x: 0<=x[0]<len(data[0]) and 0<=x[1]<len(data), ((2*x[0]-y[0],2*x[1]-y[1]) for al in next(map(lambda t: [[(i,j) for c2,i,j in t if c2 == c ] for c in {c for c,*_ in t}], [[(c,i,j) for j,l in enumerate(data) for i,c in enumerate(l) if c != "."]])) for x in al for y in al if x != y))))

def part2(data):
    return len(set(filter(lambda x: 0<=x[0]<len(data[0]) and 0<=x[1]<len(data), (((x[0]+(x[0]-y[0])*t,x[1]+(x[1]-y[1])*t) for al in next(map(lambda t: [[(i,j) for c2,i,j in t if c2 == c ] for c in {c for c,*_ in t}], [[(c,i,j) for j,l in enumerate(data) for i,c in enumerate(l) if c != "."]])) for x in al for y in al if x != y for t in range(-len(data),len(data)))))))


if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
