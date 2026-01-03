n = int(input())
ns =sorted(map(int,input().split()))
m = int(input())
ms = list(map(int,input().split()))

def binary_search(target, data):
    start=0
    end = len(data)-1

    while start<=end:
        mid = (start+end)//2
        if(data[mid]<target):
            start = mid+1
        elif(data[mid]>target):
            end = mid-1
        else:
            return 1
    return 0

for x in ms:
    print(binary_search(x,ns))