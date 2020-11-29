import unittest
from greedy import fractionalknapsack
from dynamic import knapsackDynamic
from brute_force import knapsack_bruteforce
from brute_force_fractional import fractional_knapsack_bruteforce

class KnapsacktestCase(unittest.TestCase):
    def test_greedy_fractional(self):
        weight = [10, 40, 20, 30] 
        values = [60,40,100,120]
        cap =50
        output =240

        self.assertEqual(fractionalknapsack.maximumValue(weight, values, cap), output)

    def test_dynamic(self):
        value = [2,4,3,5,5]
        weights = [3,4,1,2,6]
        caps = 12
        n = len(value)
        outs = 15
        
        self.assertEqual(knapsackDynamic(caps, weights, value, n),outs)

    def test_brute_zero_one(self):
        prof = [5, 6, 7, 2]
        wt = [4, 2, 3, 1]
        caps = 8
        outs = 15
        self.assertEqual(knapsack_bruteforce(prof, wt, caps),outs)
        
  
    def test_fractional_brute(self):
        pros = [60, 40, 100, 120]
        wt = [10, 40, 20, 30]
        capss = 50
        output = 240
        
        self.assertEqual(fractional_knapsack_bruteforce(pros,wt,capss),output)



if __name__ == "__main__":
    unittest.main()
	