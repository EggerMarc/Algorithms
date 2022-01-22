import numpy as np

def bubbleSort(unsorted, indicator = False):
    flag = True
    index = [i for i in range(len(unsorted))]
    indexed = np.column_stack((unsorted, index))

    while(flag):
        flag = False
        for i in range(0, len(unsorted)):
            try:
                if indexed[i][0] > indexed[i+1][0]:
                    indexed[i][0], indexed[i+1][0] = indexed[i+1][0], indexed[i][0]
                    indexed[i][1], indexed[i+1][1] = indexed[i+1][1], indexed[i][1]
                    flag = True
            except IndexError:
                pass
        
    if indicator == True:
        return indexed
    else:
        return indexed.T[0]

if __name__ == "__main__":
    array = [1, 31, 2, 4, 10]
    a = bubbleSort(array, True)
    print(a)
