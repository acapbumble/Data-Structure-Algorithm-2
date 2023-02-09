def distribute_power_plant_load(power_plants, loads):
    n = len(power_plants)
    m = len(loads)
    dp = [0 for j in range(m + 1)]

    power_plants.sort()
    
    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            if loads[j - 1] <= power_plants[i - 1]:
                dp[j] = max(dp[j], dp[j - 1] + loads[j - 1])
        if dp[m] == m * power_plants[i - 1]:
            break

    return dp[m]

power_plants = [100, 200, 300, 400]
loads = [50, 100, 200, 300, 400]

print("Maximum load that can be distributed:", distribute_power_plant_load(power_plants, loads))
