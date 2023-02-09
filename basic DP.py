def distribute_power_plant_load(power_plants, loads):
    n = len(power_plants)
    m = len(loads)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if loads[j - 1] <= power_plants[i - 1]:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + loads[j - 1])
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[n][m]

power_plants = [100, 200, 300, 400]
loads = [50, 100, 200, 300, 400]

print("Maximum load that can be distributed:", distribute_power_plant_load(power_plants, loads))