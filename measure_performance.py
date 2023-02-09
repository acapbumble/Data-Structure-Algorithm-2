import time

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

def distribute_power_plant_load_mod(power_plants, loads):
    n = len(power_plants)
    m = len(loads)
    power_plants = sorted(power_plants)
    dp = [0 for j in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            if loads[j - 1] <= power_plants[i - 1]:
                dp[j] = max(dp[j], dp[j - 1] + loads[j - 1])

    return dp[m]

def run_and_time_algorithm(algorithm, power_plants, loads, num_times):
    total_time = 0
    for i in range(num_times):
        start = time.time()
        algorithm(power_plants, loads)
        end = time.time()
        total_time += end - start
    return total_time / num_times

power_plants = [100, 200, 300, 400]
loads = [50, 100, 200, 300, 400]
num_times = 1000

time_original = run_and_time_algorithm(distribute_power_plant_load, power_plants, loads, num_times)
time_modified = run_and_time_algorithm(distribute_power_plant_load_mod, power_plants, loads, num_times)

percentage_difference = 100 * (time_original - time_modified) / time_original

print("\nRun Time Comparison:")
print("Algorithm\t\t\tAverage Run Time")
print("Original\t\t\t", time_original, "seconds")
print("Modified\t\t\t", time_modified, "seconds")
print("\nPercentage Difference\t", percentage_difference, "%")
