from sys import argv
from pandas import read_excel, read_csv
from math import isnan

def optimumCalculator(file):
    try:
        data = readFile(file)

        dataList = data.T.reset_index().values.tolist()
        filteredDataList = list(map(lambda x: list(filter(lambda y: isinstance(y, (int, float)) and isnan(y) == False, x)), dataList))
        
        optimumProcess = calculateOptimum(filteredDataList)

        maxOptimumProcess = list(map(lambda x: max(x), optimumProcess))

        sumOfOptimumProcess = list(map(lambda x: sum(x), optimumProcess))

        return [
            optimumProcess,
            maxOptimumProcess, 
            sumOfOptimumProcess
        ]

    except Exception as e:
        print(e)

        return e

def calculateOptimum(data):
    return list(map(lambda n: findOptimum(data[n-1], data[n]), range(1, len(data))))

def findOptimum(a, b):
    return [n*m for n in a for m in b]

def readFile(file):
    if file.lower().endswith('.csv'):
        return read_csv(file)
    
    if file.lower().endswith(('.xls', '.xlsx')):
        return read_excel(file)

if __name__ == '__main__':
    print(optimumCalculator(argv[1]))