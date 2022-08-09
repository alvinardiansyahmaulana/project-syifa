from sys import argv
from pandas import read_excel, read_csv
from math import isnan

def optimumCalculator(file):
    try:
        data = read_csv(file)
        dataList = data.T.reset_index().values.tolist()
        filteredDataList = list(map(lambda x: list(filter(lambda y: isinstance(y, (int, float)) and isnan(y) == False, x)), dataList))
        
        optimumProcess = calculateOptimum(filteredDataList)

        maxOptimumProcess = [max(x) for x in optimumProcess]

        sumOfOptimumProcess = [sum(x) for x in optimumProcess]

        return [
            optimumProcess,
            maxOptimumProcess, 
            sumOfOptimumProcess
        ]

    except Exception as e:
        print(e)

        return e

def calculateOptimum(data):
    return [findOptimum(data[n-1], data[n]) for n in range(1, len(data))]

def findOptimum(a, b):
    return [n*m for n in a for m in b]

if __name__ == '__main__':
    print(optimumCalculator(argv[1]))