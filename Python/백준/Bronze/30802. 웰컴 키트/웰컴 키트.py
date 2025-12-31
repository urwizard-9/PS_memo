n = int(input())
tshirts = list(map(int,input().split()))
t, p = map(int,input().split())

def tCount(tshirts,t):
	sum = 0
	for x in tshirts:
		if x==0:
			pass
		elif x<=t:
			sum+=1
		else:
			sum+= x//t if x%t==0 else x//t+1 
	return sum

def penCount(n,p):
	a = n//p
	b = n%p
	return a,b

print(tCount(tshirts,t))
a,b = penCount(n,p)
print(a, b)