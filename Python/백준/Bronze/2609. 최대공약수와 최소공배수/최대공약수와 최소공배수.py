from math import sqrt
def get_divisors(n):
	s = set()
	for i in range(1,int(sqrt(n))+1): #range()에 실수(float)를 전달막기 위해 int()
		if(n%i==0):
			s.add(i)
			s.add(n//i)
	return s

def get_GCD(a,b):
	set_a = get_divisors(a)
	set_b = get_divisors(b)
	return max(set_a & set_b)

def get_LCM(a, b):
	return (a * b // get_GCD(a, b))


a, b = map(int,input().split())
print(get_GCD(a,b))
print(get_LCM(a,b))


