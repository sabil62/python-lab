#this gives range of strings 0000-1111
def get_all_combinations(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def fractional_knapsack(p, w, capacity):
    assert len(p)  == len(w),"p and w must be same"

    n = len(p)
    bit_combinations = get_all_combinations(n)#0000 to 1111 all

    max_profit = 0
    #solution = ''
    for b in bit_combinations:  #0000 to 1111
        
        total_weight = 0
        for i in range(n):
            total_weight += int(b[i]) * w[i]

        
        if total_weight <= capacity:
            #calculate all the profits
            total_profit = 0
            for i in range(n):
                total_profit += int(b[i]) * p[i] #eg for 1010 (1*6+0*2+1*7+0*3)
        else:
            #dont do anything because its weight is already greater th
            total_profit = calculate_max_weight(b, capacity, p, w)
            print(total_profit)
            print(b)            
                

        if total_profit > max_profit:
            max_profit = total_profit
            #solution = b

    #return (solution, max_profit)
    return max_profit
    
    
def calculate_max_weight(bit, capacity, profit, weight):
    max_pro = 0
    n = len(weight)
    for i in range(n):
        total_wts = -weight[i] * int(bit[i]) 
        total_prof = -profit[i] * int(bit[i]) 
        for j in range(n):
            total_wts += weight[j] * int(bit[j])
            total_prof += profit[j] * int(bit[j])

            if total_wts >= capacity:
                previous_wt = total_wts - weight[j] * int(bit[j]) 
                total_wts = previous_wt 
                previous_pro = total_prof - profit[j] * int(bit[j])               
                total_prof = previous_pro
                remaining_wt = capacity - total_wts
                new_prof = previous_pro + remaining_wt * (profit[i] / weight[i])
                total_prof = new_prof
                break


        if total_prof >= max_pro:
            max_pro = total_prof

    return max_pro

if __name__ == '__main__':
    pro = [60, 40, 100, 120] 
    wt = [10, 40, 20, 30]
    capacity = 50

    #combination, max_pro = fractional_knapsack_bruteforce(pro, wt, capacity)
    max_pro = fractional_knapsack(pro, wt, capacity)
   # print(combination)
    print(max_pro)
            
    
    
           
   
