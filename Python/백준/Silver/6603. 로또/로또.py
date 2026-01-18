#조합 직접 구현방식
def function(idx,level):
    global choose, s, k    
    if(level==6):
        for x in choose:
            print(x, end=' ')
        print()
        return

    for i in range(idx,k):
        choose.append(s[i])
        function(i+1,level+1)
        choose.pop()

while True:
    data = list(map(int,input().split()))
    if(data[0]==0):
        break
    k = data[0]
    s = data[1:]

    choose = []
    function(0,0)
    print()