import time

from colors import *

def selection_sort(nums, draw_array, timeTick):
    n = len(nums)

    for i in range(n - 1):
        ind = i

        for j in range(i + 1, n):
            if nums[j] < nums[ind]:
                ind = j

            colors = [RED if x == j or x == ind else LIGHT_GREEN if x == i else WHITE for x in range(n)]
            draw_array(nums, colors)
            time.sleep(timeTick)

        nums[ind], nums[i] = nums[i], nums[ind]

