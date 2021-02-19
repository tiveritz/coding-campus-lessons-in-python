def string_operations_repetition():
    print("Hello"[1])
    print("Hello"[3:])
    print("Hello"[1:4])
    print("ll" in "Hello")
    print("LL" in "Hello")

def manual_string_slicing(string, start, end):
    print("String: " + string)
    print("Start: " + str(start))
    print("End: " + str(end))

    i = start
    for character in range(start, end):
        print(string[i], end = "")
        i += 1
