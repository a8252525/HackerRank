    
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Write your code here.

    h,m,se=map(int,s[:-2].rstrip().split(':'))
    y=s[-2:]
    h = h % 12 + (y.upper() == 'PM') * 12
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(h,m,se)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    
    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
