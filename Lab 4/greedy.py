#this is to make ratio of weight and value for fractional
class Ratio: 

	def __init__(self, weight, value, cap): 
		self.weight = weight 
		self.value = value 
		self.cap = cap
        #ratio
		self.cost = value // weight 

	def __lt__(self, other): 
		return self.cost < other.cost 

class fractionalknapsack: 
	@staticmethod
	def maximumValue(weight, value, capacity): 

		ratios = [] 
		for i in range(len(weight)): 
			ratios.append(Ratio(weight[i], value[i], i)) 

		# sorting ratios in descending order
		ratios.sort(reverse=True) 

		totalValue = 0
		for i in ratios: 
			current_weight = int(i.weight) 
			current_value = int(i.value) 
			#if capacity left then add the total value of that one
			if capacity - current_weight >= 0: 
				capacity -= current_weight 
				totalValue += current_value 
			else: 
				#if the weight is full and only fractional is allowed then, now fracture the weight
				fraction = capacity / current_weight 
				totalValue += current_value * fraction 
				capacity = int(capacity - (current_weight * fraction)) 
				break
		return totalValue 


# testing
if __name__ == "__main__": 
	weight = [10, 40, 20, 30] 
	value = [60, 40, 100, 120] 
	capacity = 50

	print(fractionalknapsack.maximumValue(weight, value, capacity) ) 



# weight = [10, 40, 20, 30] 
# value = [60, 40, 100, 120]
# capacity = 50
# greedy_fractional(capacity, weight, value)


#def greedy_fractional(capacity, weight, value):
 #   n= len(value)
  #  print(n)
   # 
    #ratio = []
   # for i in range(n):
    #    #ration = 1
     #   ration = weight[i] // value[i]
      #  ratio.append(ration)
        
        
   # ratio.sort(reverse = True)  
    #print(ratio)
    