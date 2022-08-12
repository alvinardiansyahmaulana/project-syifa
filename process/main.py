from sys import argv
from pandas import read_excel, read_csv
from math import isnan

def optimumCalculator(file):
    try:
        data = readFile(file)

        dataList = transposeDataIntoList(data)
        filteredDataList = filterDataNotNan(dataList)
        
        optimumProcess = calculateOptimum(filteredDataList)

        maxOfOptimumProcess = list(map(lambda x: max(x), optimumProcess))

        sumOfOptimumProcess = list(map(lambda x: sum(x), optimumProcess))

        return list((
            optimumProcess,
            maxOfOptimumProcess,
            sumOfOptimumProcess
        ))

    except Exception as e:

        return e


def readFile(file):
    if file.lower().endswith('.csv'):
        return read_csv(file)
    
    if file.lower().endswith(('.xls', '.xlsx')):
        return read_excel(file)

def transposeDataIntoList(data): 
    return data.T.reset_index().values.tolist()

def filterDataNotNan(data): 
    return list(map(lambda x: list(filter(lambda y: isinstance(y, (int, float)) and isnan(y) == False, x)), data))
    
def calculateOptimum(data):
    return list(map(lambda n: findOptimum(data[n-1], data[n]), range(1, len(data))))

def findOptimum(a, b):
    return [n*m for n in a for m in b]

if __name__ == '__main__':
    print(optimumCalculator(argv[1]))