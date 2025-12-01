def readfile():
    with open("input.txt","r") as file:
        return [(s[0][:-1],*s[1:]) for line in file if (s:=line.split())]

def part1(data):
    return sum(int(r)*(lambda f,r,v,i: f(f,r,v,i))(lambda f,r,v,i: r==v[0] if i==0 else (int(r)%int(v[i]) == 0 and f(f,str(int(r)//int(v[i])),v,i-1)) or (int(r)>=int(v[i]) and f(f,str(int(r)-int(v[i])),v,i-1)),r,v,len(v)-1) for r,*v in data)

def part2(data):
    return sum(int(r)*(lambda f,r,v,i: f(f,r,v,i))(lambda f,r,v,i: r==v[0] if i==0 else (len(r)!=len(v[i]) and r.endswith(v[i]) and f(f,r[:-len(v[i])],v,i-1)) or (int(r)%int(v[i]) == 0 and f(f,str(int(r)//int(v[i])),v,i-1)) or (int(r)>=int(v[i]) and f(f,str(int(r)-int(v[i])),v,i-1)),r,v,len(v)-1) for r,*v in data)

if __name__  == "__main__":
    data = readfile()
    print(part1(data))
    print(part2(data))
