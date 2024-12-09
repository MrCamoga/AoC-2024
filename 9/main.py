def readfile():
    with open("input.txt","r") as file:
        return list(map(int,file.readline().split()[0]))

def part1(data):
    l = sum([[i]*data[2*i]+[None]*data[2*i+1] if 2*i+2 <= len(data) else [i]*data[2*i] for i in range((len(data)+1)//2)],[])
    for i in range(len(l)-1,0,-1):
        if l[i] is None:
            continue
        s = l.index(None)
        if s >= i:
            break
        l[i],l[s]=l[s],l[i]
    return sum(i*x for i,x in enumerate(l) if x is not None)

def part2(data):
    l = [[i]*data[2*i]+[None]*data[2*i+1] if 2*i+2 <= len(data) else [i]*data[2*i] for i in range((len(data)+1)//2)]
    for i in range(len(data)//2,0,-1):
        for j in range(i):            
            if data[2*i] <= data[2*j+1]:
                for k in range(data[2*i]):
                    l[j][len(l[j])-data[2*j+1]+k] = i
                    l[i] = [None if x == i else x for x in l[i]]
                data[2*j+1] -= data[2*i]
                break
    return sum(i*x for i,x in enumerate(sum(l,[])) if x is not None)

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
