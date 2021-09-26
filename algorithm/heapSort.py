import time

from colors import *

def heapify(nums, n, i, draw_array, timeTick):
    largest = i

    l = 2*i + 1
    r = 2*i + 2
    colors = [RED if x == i else WHITE for x in range(len(nums))]
    draw_array(nums, colors)
    time.sleep(timeTick)

    if l < n and nums[i] < nums[l]:
        largest = l

    if r < n and nums[largest] < nums[r]:
        largest = r

    if largest != i:
        colors = [LIGHT_GREEN if x == largest or x == i else WHITE for x in range(len(nums))]
        draw_array(nums, colors)
        time.sleep(timeTick)

        nums[i], nums[largest] = nums[largest], nums[i]
        colors = [LIGHT_GREEN if x == largest or x == i else WHITE for x in range(len(nums))]
        draw_array(nums, colors)
        time.sleep(timeTick)
        heapify(nums, n, largest, draw_array, timeTick)


def heap_sort(nums, draw_array, timeTick):
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i, draw_array, timeTick)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0, draw_array, timeTick)