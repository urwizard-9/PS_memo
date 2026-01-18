#kCj
def comb(k,j):
    parents=1
    child=1

    for x in range(k,k-j,-1):
        parents *=x
    for j in range(j,0,-1):
        child *=j
    return parents//child

t = int(input())
for x in range(t):
    n,m = map(int,input().split())
    if(n>m): k,j=n,m
    else: k,j = m,n
    print(comb(k,j))
