def is_happy(n: int) -> bool:
    my_set = set()

    while True:
        summa = 0
        while n > 0:
            current_reduce = n % 10
            summa += current_reduce ** 2
            n = n // 10

        if summa in my_set:
            return False

        if summa == 1:
            return True
        else:
            my_set.add(summa)
        n = summa

print(is_happy())



