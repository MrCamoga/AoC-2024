from collections import defaultdict
from functools import reduce

def readfile():
    with open("input.txt","r") as file:
        return file.read().split(" ")

def fast(data,m):
    h = defaultdict(int)
    for x in data:
        h[x] += 1
    for i in range(m):
        for k,v in list(h.items()):
            h[k]-=v
            if k=="0":
                h["1"] += v
            elif len(k)&1:
                h[str(2024*int(k))] += v
            else:
                h[str(int(k[:len(k)//2]))] += v
                h[str(int(k[len(k)//2:]))] += v
    return sum(h.values())

def oneline(data,m):
    return (lambda f,v,i,m: f(f,v,i,m))(lambda f,v,i,m: sum(v.values()) if i==m else f(f,reduce(lambda d,x: dict(list(d.items())+[(x[0],d.get(x[0],0)+x[1])]), sum([[("1",c)] if x=="0" else [(str(2024*int(x)),c)] if len(x)&1 else [(str(int(x[:len(x)//2])),c),(str(int(x[len(x)//2:])),c)] for x,c in v.items()],[]), {}),i+1,m), {x:data.count(x) for x in data}, 0, m)
    
if __name__  == "__main__":
    data = readfile()
    print(fast(data,25))
    print(fast(data,75))
    print(oneline(data,25))
    print(oneline(data,75))
