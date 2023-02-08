def power_plant_load_distribution(power_plants, total_load):
    n = len(power_plants)
    dp = [ [0 for j in range(total_load + 1)] for i in range(n + 1)]
  
    for i in range(1, n + 1):
        for j in range(1, total_load + 1):
            if j < power_plants[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - power_plants[i - 1]] + power_plants[i - 1])
  
    return dp[n][total_load]

# test with sample data
power_plants = [100, 300, 200, 400]
total_load = 800
print("Maximum load distribution:", power_plant_load_distribution(power_plants, total_load))