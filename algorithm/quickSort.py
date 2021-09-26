import time

from colors import *

def parition(nums, l, r, draw_array, timeTick):
    i = l - 1
    piv = nums[r]

    for j in range(l, r):
        if nums[j] <= piv:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

        colors = [RED if x == l or x == r else LIGHT_GREEN if x == piv else BLUE if x == i or x == j else WHITE for x in range(len(nums))]
        draw_array(nums, colors)
        time.sleep(timeTick)

    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

def quick_sort(nums, l, r, draw_array, timeTick):
    if (len(nums) == 1):
        return

    if (l >= r):
        return

    p = parition(nums, l, r, draw_array, timeTick)

    colors = [RED if x == l or x == r else LIGHT_GREEN if x == p else WHITE for x in range(len(nums))]
    draw_array(nums, colors)
    time.sleep(timeTick)

    quick_sort(nums, l, p - 1, draw_array, timeTick)
    quick_sort(nums, p + 1, r, draw_array, timeTick)
