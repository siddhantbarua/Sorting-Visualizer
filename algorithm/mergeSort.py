import time

from colors import *

def merge(nums, l, mid, r, draw_array, timeTick):
    left = nums[l : mid + 1]
    right = nums[mid + 1 : r + 1]

    n1 = len(left)
    n2 = len(right)

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] >= right[j]:
            nums[k] = right[j]
            j += 1

        else:
            nums[k] = left[i]
            i += 1

        colors = [RED if x == l or x == r else LIGHT_GREEN if x == mid else BLUE if x == k else WHITE for x in range(len(nums))]
        k += 1
        draw_array(nums, colors)
        time.sleep(timeTick)

        

    while i < n1:
        nums[k] = left[i]
        i += 1
        k += 1
        colors = [RED if x == l or x == r else LIGHT_GREEN if x == mid else BLUE if x == k else WHITE for x in range(len(nums))]
        draw_array(nums, colors)
        time.sleep(timeTick)

    while j < n2:
        nums[k] = right[j]
        j += 1
        k += 1
        colors = [RED if x == l or x == r else LIGHT_GREEN if x == mid else BLUE if x == k else WHITE for x in range(len(nums))]
        draw_array(nums, colors)
        time.sleep(timeTick)


def merge_sort(nums, l, r, draw_array, timeTick):

    if l >= r:
        return

    mid = l + (r - l) // 2

    merge_sort(nums, l, mid, draw_array, timeTick)
    merge_sort(nums, mid + 1, r, draw_array, timeTick)

    merge(nums, l, mid, r, draw_array, timeTick)