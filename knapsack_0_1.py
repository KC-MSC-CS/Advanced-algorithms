# A Bottom-UP approach based 0/1 Knapsack
# Returns the maximum value that can be put in a knapsack of capacity W
 
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
 
# Driver code
val = [60, 100, 120, 100, 80, 130, 50, 70, 60, 70, 60, 40, 50, 60, 40, 50, 60]
wt = [10, 20, 30, 40, 60, 90, 80, 20, 40, 50, 50, 30,20, 10, 50, 50, 60]
W = 250
n = len(val)
import time
# starting time
start = time.time()
print (knapSack(W, wt, val, n))
# end time
end = time.time()
# total time taken
print(f"Runtime of the program is {end - start}")