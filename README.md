# Modified Dynamic Programming Algorithm (Distribution of power plant load)

## How to run the codes
1) Open the basic & modified code
2) click on run (depends on what compliler you use)

## Abstract
This report is about modifying a dynamic programming algorithm to find the maximum load that can be distributed in a power plant load, with the purpose of optimizing it. This report is referenced by an article I chose [Modified Dynamic Programming Algorithm and Its Application in
Distribution of Power Plant Load](https://www.e3s-conferences.org/articles/e3sconf/pdf/2019/62/e3sconf_icbte2019_01005.pdf)

## Introduction
There are two set of codes. Basic and the modified version of it. The purpose of this modification is to optimize the code by reducing the calculation time and memory usage. The rest of the report will show you how it is done, the performance of each code and its comparison with a conclusion.

## Basic Dynamic Programming
1) Initialize two variables n and m with the length of the power_plants and loads arrays respectively.
2) Create a 2D array dp with n + 1 rows and m + 1 columns. This array will be used to store the intermediate results during the calculation.
3) Use a nested loop to iterate over the power_plants and loads arrays. The outer loop ranges from 1 to n + 1, and the inner loop ranges from 1 to m + 1.
4) For each iteration of the loop, check if the current load is less than or equal to the current power plant capacity.

- If it is, calculate the maximum value between the current cell's value and the value from the previous cell plus the current load.
- If it is not, set the current cell's value to the value from the previous cell.
- Repeat steps 4 for all cells in the dp array.

5) Return the value in the last cell of the dp array, which represents the maximum load that can be distributed among the power plants.
6) Finally, the maximum load is printed by calling the distribute_power_plant_load function with power_plants and loads as arguments.

