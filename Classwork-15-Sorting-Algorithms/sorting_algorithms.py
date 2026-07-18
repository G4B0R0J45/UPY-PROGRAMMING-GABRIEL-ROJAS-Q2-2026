import random
import stddraw
from color import Color


def bubble_sort(numbers):
    # Get the length of the array
    n = len(numbers)

    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]


def insertion_sort(numbers):
    # Get the length of the array
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = key


def selection_sort(numbers):
    # Get the length of the array
    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n

    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)


def bubble_sort_animated(numbers):
    # CONFIG - canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    # Get the length of the array
    n = len(numbers)

    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            # DRAW the rectangles before the swap
            draw_bars(numbers, selected=(pair, pair + 1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
                # DRAW the rectangles after the swap
                draw_bars(numbers, selected=(pair, pair + 1))

    draw_bars(numbers)
    stddraw.show()


def insertion_sort_animated(numbers):
    # CONFIG - canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    # Get the length of the array
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        # DRAW the element that is about to be inserted
        draw_bars(numbers, selected=(i,))
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1
            # DRAW the array after shifting one element to the right
            draw_bars(numbers, selected=(j + 1,))
        numbers[j + 1] = key
        # DRAW the array after dropping the key into its place
        draw_bars(numbers, selected=(j + 1,))

    draw_bars(numbers)
    stddraw.show()


def selection_sort_animated(numbers):
    # CONFIG - canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    # Get the length of the array
    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # DRAW the current minimum and the element being compared
            draw_bars(numbers, selected=(min_index, j))
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        # DRAW the array after placing the minimum in its final spot
        draw_bars(numbers, selected=(i, min_index))

    draw_bars(numbers)
    stddraw.show()


# INPUT
numbers = [random.randint(0, 100) for _ in range(10)]
print(f"Before sorting: {numbers}")

# PROCESS
# Run one animated sorting algorithm (swap the call to try the others)
bubble_sort_animated(numbers)
# insertion_sort_animated(numbers)
# selection_sort_animated(numbers)

# OUTPUT
print(f"After sorting:  {numbers}")
