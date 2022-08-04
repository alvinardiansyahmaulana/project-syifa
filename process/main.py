from sys import argv

def optimumCalculator(data):
    try:
        process = tuple((
            tuple((range(1,4))), #process A
            tuple((range(5,8))), #process B
            tuple((range(9,12))), #process C
            tuple((range(13,16))), #process D
        ))

        optimumProcess = calculateOptimum(process)

        maxOptimumProcess = [max(x) for x in optimumProcess]

        sumOfOptimumProcess = [sum(x) for x in optimumProcess]
        
        return [optimumProcess, maxOptimumProcess, sumOfOptimumProcess]
    except Exception as e:
        print(e)

        return e

def calculateOptimum(process):
    return [findOptimum(process[n-1], process[n]) for n in range(1, len(process))]

def findOptimum(a, b):
    return [n*m for n in a for m in b]

if __name__ == '__main__':
    print(optimumCalculator(argv[1]))