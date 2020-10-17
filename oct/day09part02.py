from day09part01 import bubble_sort
# import all: import day09part01 -> the call with: day09part01.bubble_sort()

def recursion_counter(start, end):
        counter = start
        print(counter)
        
        if (counter < end-1):
            counter += 1
            recursion_counter(counter, end)

def function_call_from_other_file():
    print(bubble_sort([6, 5, 4, 3, 2, 0]))


# recursion_counter(4, 10)
# function_call_from_other_file()