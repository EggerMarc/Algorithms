from bubblesort import bubbleSort
import numpy as np
import header

class KnapsackFrac:
    def __init__(self, capacity, weights, values):
        self.capacity = capacity
        self.weights = weights
        self.values = values
        
        if (self.weights == None and self.values == None and len(self.weights) != len(self.values) and self.capacity < 0):
            raise Exception("Error initilizing class")
        self.efficiencyValues = [sum(i)/len(i) for i in zip(weights,values)]

    def model(self):
        #first we want to fractionalize breakeven
        ordered = bubbleSort(self.efficiencyValues, True)
        x_values = np.zeros(ordered.shape)

        k = self.capacity
        for i in range(len(ordered)):
            if ordered[i][0] < k:
                x_values[i][0], x_values[i][1] = 1, ordered[i][1]
                k -= ordered[i][0]

        print(x_values)
        return x_values





if __name__ == '__main__':
    w = [3,1,3,4,2]
    v = [2,2,4,5,3]
    k = 3

    tryout1 = KnapsackFrac(k,w,v).model()
    