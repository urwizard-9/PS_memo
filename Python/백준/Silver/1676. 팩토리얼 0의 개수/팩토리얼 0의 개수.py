def factorial(n):
    result =1
    for x in range(2,n+1):
        result *=x

    return result

n = int(input())
result = str(factorial(n))
cnt =0
for x in range(len(result)-1,0,-1):
    if(result[x]!="0"):
        break
    cnt+=1

print(cnt)

