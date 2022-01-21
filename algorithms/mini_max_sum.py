#!/bin/python3

import sys

arr = list(map(int, input().rstrip().split()))
# arr = [5, 3, 4, 2, 1]

total = sum(arr)
arr.sort()
print (total-arr[-1], total-arr[0])