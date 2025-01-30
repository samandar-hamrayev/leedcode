res = []
num = 1000
while num > 0:
    res.append(num % 10)
    num //= 10

print(res[::-1])