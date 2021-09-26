import time

from colors import *

def insert_sort(nums, draw_array, timeTick):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
            colors = [RED if x == j or x == j + 1 else LIGHT_GREEN if x == i else WHITE for x in range(n)]
            draw_array(nums, colors)
            time.sleep(timeTick)

        nums[j + 1] = key

