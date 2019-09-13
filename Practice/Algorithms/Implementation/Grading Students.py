#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def ceil5(x):
    return ((x//5)+1)*5
def gradingStudents(grades):
    # Write your code here
    ans=[]
    temp=0
    
    for i in grades:
        if i < 38:
            ans.append(i)
        else:
            if ceil5(i)-i>2:
                ans.append(i)
            else:
                ans.append(ceil5(i))


    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
