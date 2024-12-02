def readfile():
    data = [],[]
    with open("input.txt","r") as file:
        for line in file:
            v = line.split()
            data[0].append(int(v[0]))
            data[1].append(int(v[1]))
    return data


def part1(data):
    data[0].sort()
    data[1].sort()
    return sum(abs(x-y) for x,y in zip(*data))

def part2(data):
    hist = dict()
    for x in data[1]:
        hist[x] = hist.get(x,0)+1
    return sum(x*hist.get(x,0) for x in data[0])

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
