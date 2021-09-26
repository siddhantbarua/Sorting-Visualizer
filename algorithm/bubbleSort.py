import time

from colors import *

def bubble_sort(nums, draw_array, timeTick):
    n = len(nums)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                colors = [RED if x == j or x == j + 1 else WHITE for x in range(n)]
                draw_array(nums, colors)
                time.sleep(timeTick)

