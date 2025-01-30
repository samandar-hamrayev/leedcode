def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies_sum = n
    i = 1

    while i < n:
        if ratings[i] == ratings[i-1]:
            i += 1
            continue

        temp_peak = 0
        while i < n and ratings[i] > ratings[i-1]:
            temp_peak += 1
            candies_sum += temp_peak
            i += 1

        if i == n:
            return candies_sum

        temp_valley = 0
        while i < n and ratings[i] < ratings[i-1]:
            temp_valley += 1
            candies_sum += temp_valley
            i += 1

        candies_sum -= min(temp_peak, temp_valley)

    return candies_sum

