#bottom-up 방식
ans = ['' for _ in range(13)]
ans[0] = '-'

for i in range(1, 13):
	ans[i] = ans[i-1] + (' ' * (3 ** (i-1))) + ans[i-1]

while True:
	try:
		N = int(input())
		print(ans[N])
	except:  #적은 입력을 다 받고 나면 except 구문이 실행되서 이때 break로 while문 빠져나옴

		break
