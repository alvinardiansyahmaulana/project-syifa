import sys

process = tuple((
    tuple((range(3,8))), #process A
    tuple((range(6,16))), #process B
    tuple((range(2,9))), #process C
    tuple((range(10,20))), #process D
))

optimumProcess = calculateOptimum(process)

maxOptimumProcess = [max(x) for x in optimumProcess]

sumOfOptimumProcess = [sum(x) for x in optimumProcess]

print(sumOfOptimumProcess)

sys.stdout.flush()

def calculateOptimum(process):
    return [findOptimum(process[n-1], process[n]) for n in range(1, len(process))]

def findOptimum(a, b):
    return [n*m for n in a for m in b]