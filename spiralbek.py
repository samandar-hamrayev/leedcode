import datetime

def decorator(func):
    def wrapper(*args):
        start = datetime.datetime.now()
        func(*args)
        end = datetime.datetime.now()
        return end - start
    return wrapper



def make_spiral(m, n):
    matrix = [[0] * n for _ in range(m)]
    left, top, right, bottom = 0, 0, n-1, m-1
    def backer(left, top, right, bottom, value):
        if value > m * n:
            return
        for i in range(left, right + 1):
            matrix[top][i] = value
            value += 1
        top +=1

        for i in range(top, bottom+1):
            matrix[i][right] = value
            value += 1
        right -=1

        if top <= bottom:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = value
                value += 1
            bottom -=1

        if left <= right:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = value
                value += 1
            left += 1
        backer(left, top, right, bottom, value)

    backer(0, 0, n-1, m-1, 1)
    for row in matrix:
        print(row)


dek = decorator(make_spiral)
print(dek(10, 10))








