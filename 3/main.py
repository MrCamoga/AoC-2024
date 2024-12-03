import re

def readfile():
    with open("input.txt","r") as file:
        return "".join(file)

def part1(data):
    return sum(int(x)*int(y) for x,y in re.findall("(?<!do_not_)mul\((\d+),(\d+)\)",data))

def part2(data, o=False):
    return sum(int(i[0])*int(i[1]) for i in (list(filter(None,l)) for l in re.findall("(d)o\(\)|d(o)n't\(\)|mul\((\d+),(\d+)\)",data)) if not (o := o if len(i) == 2 else i[0] == "o") and len(i)==2)

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
