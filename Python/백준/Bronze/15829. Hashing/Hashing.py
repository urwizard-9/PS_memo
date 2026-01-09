#기본 정보 입력받기
l = int(input())
string = input()

r = 31
m = 1234567891

#문자열을 수열로 변환
alphabets = {}
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i, alpha in enumerate(letters, start=1):
    alphabets[alpha] = i

#해시함수 구현
def hash(filter):
    result = 0
    filter = 0
    i = 0
    for s in string:
        filter = alphabets.get(s)
        result += filter*r**i
        i+=1
    return result%m

print(hash(filter))