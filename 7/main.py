from itertools import product
from functools import reduce

def readfile():
    with open("input.txt","r") as file:
        return [(s[0][:-1],*s[1:]) for line in file if (s:=line.split())]

def part1(data):
    return sum(int(r)*any(r==reduce(lambda a,b: str(eval(a+b)), [b+a for a,b in zip(v,op)], s) for op in product("*+",repeat=len(v))) for r, s, *v in data)

def part2(data):
    return sum(int(r)*any(r==reduce(lambda a,b: str(eval(a+b)) if b[0] != "|" else a+b[1:], [b+a for a,b in zip(v,op)], s) for op in product("|*+",repeat=len(v))) for r, s, *v in data)

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
