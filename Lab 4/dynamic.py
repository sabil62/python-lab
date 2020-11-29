
# Dynamic programming for 0/1 knapsack problem
def knapsackDynamic(capacity, weight, value, n):
    #making 2 by 2 matrix of all 0 (capcity * n)
   table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
   #Table in bottom up manner
   for i in range(n + 1):
      for c in range(capacity + 1):
          #this is making the side value of the table as 0 (weight 0 and value 0)
         if i == 0 or c == 0:
            table[i][c] = 0
            #if the current weight is smaller than total capcaity
         elif weight[i-1] <= c:
             #max(profit+ total baki profit, or upper cell ko profit)
            table[i][c] = max(value[i-1] + table[i-1][c-weight[i-1]], table[i-1][c])
         else:
            table[i][c] = table[i-1][c]
   return table[n][capacity]
#Main
value = [2,4,3,5,5]
weight = [3,4,1,2,6]
capacity = 12
n = len(value)
print(knapsackDynamic(capacity, weight, value, n))

