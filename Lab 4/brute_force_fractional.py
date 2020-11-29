#this gives range of strings 0000-1111
def get_all_combinations(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def fractional_knapsack_bruteforce(p, w, capacity):
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
            
            total_profit = 0
            anchor = 0
            anchor_weight = 0
            anchor_profit = 0
            for i in range(n):             
                anchor += 1
                anchor_weight += int(b[i]) * w[i]
                anchor_profit += int(b[i]) * p[i]
                if(anchor_weight >= capacity):
                    #print(b)
                    previous_weight =anchor_weight - int(b[i]) * w[i]#previous anchor_weight
                    capacity_left = capacity- previous_weight
                    previous_profit = anchor_profit - int(b[i]) * p[i]
                    new_profit = previous_profit + capacity_left * (p[i] // w[i])
                    total_profit = new_profit 
                    
                    break
                
           # print(anchor)
            #print(total_profit)
            #print("-----------------------")
                

        if total_profit > max_profit:
            max_profit = total_profit
            #solution = b

    #return (solution, max_profit)
    return max_profit

if __name__ == '__main__':
    pro = [60, 40, 100, 120] 
    wt = [10, 40, 20, 30]
    capacity = 50

    #combination, max_pro = fractional_knapsack_bruteforce(pro, wt, capacity)
    max_pro = fractional_knapsack_bruteforce(pro, wt, capacity)
   # print(combination)
    print(max_pro)
