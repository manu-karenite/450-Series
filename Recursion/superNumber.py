# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def getAns(num):
    if num <= 9:
        return num

    sum = 0
    for x in str(num):
        sum = sum+int(x)
    return getAns(sum)


def superDigit(n, k):
    # Write your code here
    sum = 0
    for x in str(n):
        sum = sum+int(x)

    q = int(sum*k)
    print(q)
    ans = getAns(q)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
