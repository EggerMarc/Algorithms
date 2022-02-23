from functools import cache
from logging import exception
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')

class Fibonacci:
    def __init__(self,iter):
        self.iter = iter
        print(iter)

    def slowFibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return self.slowFibonnaci(self, n-1) + self.slowFibonacci(self,n-2)

@cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)

def fib_array(n):
    fib = np.zeros(n)
    try:
        fib[1] += 1
    except:
        IndexError
    if len(fib) > 2:
        for i in range(2, fib.shape[0]):
            fib[i] += fib[i-1] + fib[i-2]
    elif len(fib) == 0 or len(fib) == 1:
        pass
    else:
        raise Exception("Unrecognized sequence size")
    return fib

if __name__ == "__main__":
    #print(Fibonacci(10).slowFibonacci(10))
    ans = fib(100)
    #plt.figure()
    #plt.plot(ans)
    print(ans)
    # plt.show()