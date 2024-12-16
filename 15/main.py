import sys
sys.setrecursionlimit(100000)

def readfile():
    with open("input.txt","r") as file1, open("input2.txt","r") as file2:
        return [[c for c in line if c!="\n"] for line in file1], list(map(lambda c: (ord(c)%11-2)&3, file2.readline()))

def part1(m,movs):
    return (lambda f,pos,it: f(f,pos,it))(lambda f,pos,it: 1 if m[pos[1]].__setitem__(pos[0],".") or it == len(movs) else (lambda newpos,c: f(f,pos,it+1) if c == "#" else f(f,newpos,it+1) if c == "." else (lambda l: m[l[2]].__setitem__(l[1],"O") or f(f,newpos,it+1) if l[0] == "." else f(f,pos,it+1))(next((m[j][i],i,j) for k in range(2,100) if (i:=pos[0]+((0,-1),(1,0),(0,1),(-1,0))[movs[it]][0]*k) and (j:=pos[1]+((0,-1),(1,0),(0,1),(-1,0))[movs[it]][1]*k) and m[j][i] != "O")))(*(lambda np: (np, m[np[1]][np[0]]))(tuple(pos[i]+((0,-1),(1,0),(0,1),(-1,0))[movs[it]][i] for i in range(2)))), next((i,j) for j in range(len(m)) for i in range(len(m[0])) if m[j][i]=="@"),0) * sum(i+100*j for j in range(len(m)) for i in range(len(m[0])) if m[j][i]=="O")

def part2(data):
    return 

if __name__  == "__main__":
    data = readfile()
    print(part1([[c for c in line] for line in data[0]],data[1]))
    print(part2(data))
