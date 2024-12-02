def readfile():
    with open("input.txt","r") as file:
        return [list(map(int, line.split())) for line in file]


def part1(data):
    return sum(all(x[1] for x in d) and all(d[0][0] == x[0] for x in d) for l in data if (d := [(l[i] > l[i+1], 0 < abs(l[i]-l[i+1]) < 4) for i in range(len(l)-1)]))
            
def part2(data):
    return sum(any(all(x[1] for x in d2) and all(d2[0][0] == x[0] for x in d2) for i in range(len(l)+1) if (d := [x for j,x in enumerate(l) if i!=j], d2 := [(d[i] > d[i+1], 0 < abs(d[i]-d[i+1]) < 4) for i in range(len(d)-1)])) for l in data )


if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
