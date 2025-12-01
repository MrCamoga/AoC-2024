from functools import cmp_to_key

def readfile():
    with open("input.txt","r") as file1, open("input2.txt","r") as file2:
        return [list(map(int,line.split("|"))) for line in file1], [list(map(int,line.split(","))) for line in file2]

def part1(data1,data2):
    return sum(l[len(l)>>1] for l in data2 if all(x not in l or y not in l or l.index(x) < l.index(y) for x,y in data1))

def part2(data1,data2):
    return sum(sorted(l,key=cmp_to_key(lambda a,b: (-1 if [a,b] in data1 else 1) if ([a,b] in data1 or [b,a] in data1) else 0))[len(l)>>1] for l in data2 if any(x in l and y in l and l.index(x) > l.index(y) for x,y in data1))

if __name__  == "__main__":
    data = readfile()
    print(part1(*data))
    print(part2(*data))
