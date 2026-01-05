from collections import deque

s = deque()
n=int(input())
for x in range(n):
    command = list(input().split())
    order = command[0]
    if(command[0]=="push"):
        num = int(command[1])
        s.append(num)
    elif(command[0]=="top"):
        print(s[-1] if len(s)>0 else -1 )
    elif(command[0]=="size"):
        print(len(s))
    elif(command[0]=="empty"):
        print(1 if len(s)<=0 else 0)
    elif(command[0]=="pop"):
        print(s.pop() if len(s)>0 else -1)