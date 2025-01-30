n = int(input())
daraja = 0

while n > 0:
    power = 1
    while power * 2 <= n:
        power *= 2

    start = n - power
    end = power * 2 - n

    n = min(start, end)
    daraja += 1

print(daraja)








