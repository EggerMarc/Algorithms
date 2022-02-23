import numpy as np

class Knapsack:
    def __init__(self, capacity, weights, values):
        self.capacity = capacity
        self.weights = weights
        self.values = values
        if (self.weights == None and self.values == None and len(self.weights) != len(self.values) and self.capacity < 0):
            raise Exception("Error initilizing class")

    def model(self):
        N_count = len(self.weights)

        df = np.zeros((len(self.weights),len(self.values)))

        for i in range(0,N_count):
            
            weight = self.weights[i]
            value = self.values[i]

            for n in range(self.capacity):
                try:
                    df[i+1][n+1] += df[i][n+1]
                    if (n+1 > weight and df[i+1][n + 1 - weight] + value > df[i+1][n+1]):
                        df[i+1][n+1] += df[i][n] + value
                except:
                    IndexError
        return df


if __name__ == '__main__':
    w = [3,1,3,4,2]
    v = [2,2,4,5,3]
    k = 12

    tryout1 = Knapsack(k,w,v)
    print(tryout1.model())
