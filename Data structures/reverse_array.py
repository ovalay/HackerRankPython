def reverse_Array(nums):
    # print(*nums[::-1])  either of these will work
    print(*reversed(nums))


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
reverse_Array(arr)
