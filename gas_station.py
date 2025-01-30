def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    jami_gaz = joriy_gaz = boshlash = 0

    for i in range(len(gas)):
        qoshimcha = gas[i] - cost[i]
        jami_gaz += qoshimcha
        joriy_gaz += qoshimcha

        if joriy_gaz < 0:
            joriy_gaz = 0
            boshlash += 1


    return - 1 if jami_gaz < 0 else boshlash

print(canCompleteCircuit(gas = [5,1,2,3,4], cost = [4,4,1,5,1]))


