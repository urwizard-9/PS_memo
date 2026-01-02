def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

anwer=0
inputs = [input() for i in range(3)]
for x in range(0,3):
    if(inputs[x].isdigit()):
        answer = int(inputs[x])+(3-x)
        break

print(fizzbuzz(answer))