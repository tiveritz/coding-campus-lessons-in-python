def recursion_counter(start, end):
    counter = start
    print(counter)
    
    if (counter < end-1):
        counter += 1
        recursion_counter(counter, end)
