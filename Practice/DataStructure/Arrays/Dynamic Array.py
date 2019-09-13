# problem:https://www.hackerrank.com/challenges/dynamic-array/problem

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastanswer=0
    s=[]
    for _ in range(n):
        s.append([])#บ๋ตุ
    anslist=[]
    for i in range(q):
        x=queries[i][1]
        if queries[i][0]==1:
            index=(x^lastanswer)%n
            s[index].append(queries[i][2])
        elif queries[i][0]==2:
            index=(x^lastanswer)%n
            subindex=(queries[i][2])%(len(s[index]))
            lastanswer=s[index][subindex]
            anslist.append(lastanswer)
    return anslist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()