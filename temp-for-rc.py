import math


class CorrelationCalculator:
    def __init__(self, points):
        self.points = points
        self.n = len(points)
        self.sumX = sum(p[0] for p in points)
        self.sumY = sum(p[1] for p in points)
        self.sumXY = sum(p[0] * p[1] for p in points)
        self.sumX2 = sum(p[0] ** 2 for p in points)
        self.sumY2 = sum(p[1] ** 2 for p in points)

    def update_point(self, i, a, b):
        old_x, old_y = self.points[i]
        self.sumX += a - old_x
        self.sumY += b - old_y
        self.sumXY += a * b - old_x * old_y
        self.sumX2 += a ** 2 - old_x ** 2
        self.sumY2 += b ** 2 - old_y ** 2
        self.points[i] = [a, b]

    def calculate_correlation(self, l, r):
        sub_points = self.points[l:r]
        n = len(sub_points)
        if n < 2:
            return "undefined"

        sumX = sum(p[0] for p in sub_points)
        sumY = sum(p[1] for p in sub_points)
        sumXY = sum(p[0] * p[1] for p in sub_points)
        sumX2 = sum(p[0] ** 2 for p in sub_points)
        sumY2 = sum(p[1] ** 2 for p in sub_points)

        numerator = n * sumXY - sumX * sumY
        denominator = math.sqrt((n * sumX2 - sumX ** 2) * (n * sumY2 - sumY ** 2))

        if denominator == 0:
            if numerator > 0:
                return "inf"
            elif numerator < 0:
                return "-inf"
            else:
                return "undefined"

        return f"{numerator / denominator:.8f}"


# Input o'qish
n, q = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
calculator = CorrelationCalculator(points)

# So'rovlarni o'qish va ishlash
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, a, b = query[1] - 1, query[2], query[3]
        calculator.update_point(i, a, b)
    elif query[0] == 2:
        l, r = query[1] - 1, query[2]
        result = calculator.calculate_correlation(l, r)
        print(result)