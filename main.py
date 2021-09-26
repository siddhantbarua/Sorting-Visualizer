from algorithm.bubbleSort import bubble_sort
from tkinter import *
from tkinter import ttk

from colors import *

from algorithm.bubbleSort import bubble_sort
from algorithm.insertSort import insert_sort
from algorithm.selectionSort import selection_sort
from algorithm.mergeSort import merge_sort
from algorithm.quickSort import quick_sort
from algorithm.heapSort import heap_sort


import random
import threading

window = Tk()
window.title("Visualisation of Sorting Algorithms")
window.maxsize(1000, 700)
window.config(bg=BLACK)

# Sorting algorithm used
algo = StringVar()
algo_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort", "Heap Sort"]

# Sorting speed
speed = DoubleVar()

# Numbers to sort
nums = []

# Number of elements
n = 100

canvas_width = 800
canvas_height = 400

# To draw the array on the window
def draw_array(nums, colors):
    n = int(num_entry.get())

    canvas.delete("all")  #Clear canvas
    width = canvas_width / (n + 1)

    offset = 4
    spacing = 2
    
    max_num = max(nums)
    noramlised_nums = [i / max_num for i in nums]

    for i, ht in enumerate(noramlised_nums):
        x0 = i * width + offset + spacing
        y0 = canvas_height - ht * (canvas_height)

        x1 = (i + 1) * width + offset

        canvas.create_rectangle(x0, y0, x1, canvas_height, fill=colors[i])

    window.update_idletasks()

# To generate random numbers in array
def generate_array():
    global nums
    n = int(num_entry.get())

    nums = []

    for i in range(n):
        rand = random.randint(0, 150)
        nums.append(rand)

    draw_array(nums, [WHITE for x in range(n)])

# Set speed of sorting
def set_speed():
    return speed_scale.get()

# Sorting array
def sort():
    n = int(num_entry.get())

    global nums
    timeTick = set_speed()
    curr_algo = algo_menu.get()

    if curr_algo == "Bubble Sort":
        bubble_sort(nums, draw_array, timeTick)

    if curr_algo == "Insertion Sort":
        insert_sort(nums, draw_array, timeTick)

    if curr_algo == "Selection Sort":
        selection_sort(nums, draw_array, timeTick)

    if curr_algo == "Merge Sort":
        merge_sort(nums, 0, n - 1, draw_array, timeTick)
    
    if curr_algo == "Quick Sort":
        quick_sort(nums, 0, n - 1, draw_array, timeTick)

    if curr_algo == "Heap Sort":
        heap_sort(nums,draw_array, timeTick)

    draw_array(nums, [BLUE for x in range(n)])

## UI stuff

frm = Frame(window, width=900, height=300, bg=DARK_GRAY)
frm.grid(row=0, column=0, padx=10, pady=5)

# Algo DropDown
lbl_algo = Label(frm, text="Sorting Algorithm: ", bg=WHITE, fg=BLACK)
lbl_algo.grid(row=0, column=0, padx=10, pady=5, sticky=W)

algo_menu = ttk.Combobox(frm, textvariable=algo, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)    # Default Value

# Speed DropDown
lbl_speed = Label(frm, text="Sorting Speed: ", bg=WHITE, fg=BLACK)
lbl_speed.grid(row=1, column=0, padx=10, pady=5, sticky=W)

speed_scale = ttk.Scale(frm, variable=speed, from_=1.0, to=0.001)
speed_scale.grid(row=1, column=1, padx=5, pady=5)
speed_scale.set(0.01)

# Number of elements
lbl_num = Label(frm, text="Number of Elements: ", bg=WHITE, fg=BLACK)
lbl_num.grid(row=2, column=0, padx=10, pady=5, sticky=W)

num_entry = ttk.Entry(frm)
num_entry.grid(row=2, column=1, padx=5, pady=5)
num_entry.insert(0, '100')

# Button to generate array
btn_gen = Button(frm, text="Generate Array", command=generate_array, bg=LIGHT_GRAY, fg=BLACK)
btn_gen.grid(row=3, column=0, padx=5, pady=5)

# Button for Sorting
btn_sort = Button(frm, text="Sort Array", command=sort, bg=LIGHT_GRAY, fg=BLACK)
btn_sort.grid(row=3, column=1, padx=5, pady=5)

# Draw array
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg=BLACK)
canvas.grid(row=4, column=0, padx=10, pady=5)

# Event Loop
window.mainloop()
