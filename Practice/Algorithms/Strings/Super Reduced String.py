# Problem: https://www.hackerrank.com/challenges/reduced-string/problem

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    pattern=re.compile(r'(\w)(\1)')
    match=pattern.search(s)
    while match:
        s=re.sub(match.group(),'',s)
        match=pattern.search(s)
    if s:
        return s
    else:
        return 'Empty String'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(str(s))

    fptr.write(result + '\n')

    fptr.close()
