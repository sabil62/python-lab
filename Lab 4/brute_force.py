#this gives range of strings 0000-1111
def get_all_combinations(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def knapsack_bruteforce(p, wt, capacity):
    assert len(p)  == len(wt),"p and wt must be same"

    n = len(p)
    bit_combinations = get_all_combinations(n)#0000 to 1111 all

    max_profit = 0
    #solution = ''
    for b in bit_combinations:  #0000 to 1111
        #calculate all the profits
        total_profit = 0
        for i in range(n):
            total_profit += int(b[i]) * p[i] #eg for 1010 (1*6+0*2+1*7+0*3)

        total_weight = 0
        for i in range(n):
            total_weight += int(b[i]) * wt[i]


        if total_weight <= capacity and total_profit > max_profit:
            max_profit = total_profit
           # solution = b

    #return (solution, max_profit)
    return max_profit

if __name__ == '__main__':    
    wt = [4, 2, 3, 1]
    pro = [5, 6, 7, 2]
    caps = 8

   # combination, max_pro = knapsack_bruteforce(pro, wt, caps)
    max_pro = knapsack_bruteforce(pro, wt, caps)
   # print(combination)
    print(max_pro)







# # 0/1 Knapsack problem
# def knapsack(capacity, weight, value, n):
#    # initial conditions where if total is 0 and capacity is 0 returns 0
#    if n == 0 or capacity == 0 :
#       return 0
#    # dont include the ones whose weight is larger than capacity, so go n-1
#    if (weight[n-1] > capacity):
#       return knapsack(capacity, weight, value, n-1)
#    # this calculates recursively , imagine tree
#    else:
#       return max(value[n-1] + knapsack(capacity-weight[n-1], weight, value, n-1),
#          knapsack(capacity, weight, value, n-1))
# # Testing 
# value = [2,4,3,5,5]
# weight = [3,4,1,2,6]
# capacity = 12
# n = len(value)
# print (knapsack(capacity, weight, value, n))

