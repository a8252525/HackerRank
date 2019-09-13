#problem:https://www.hackerrank.com/challenges/crush/problem

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l=[]
    temp=0

    for _ in range(n):
        l.append(0)

    for query in queries:
        l[query[0]-1]+=query[2]
        if query[1]<n:
            l[query[1]]-=query[2]

    max_value=0
    
    for number in l:
        temp+=number
        if temp > max_value:
            max_value=temp
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
