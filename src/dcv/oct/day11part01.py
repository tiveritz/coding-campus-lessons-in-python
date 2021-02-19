# Calculate the faculty of a given number
# Example 5! should result to 120
# Mathematical problem: 5! = 4!

def recursion_faculty(n):
    print("faculty" + str(n) + " begin")
    result = 1

    if (n > 1):
        result = n * recursion_faculty(n - 1)

    print("faculty " + str(n) + " end")
    return result


# Same example without recursion

def faculty_without_recursion(n):
    result = n
    i = n

    while (i > 1):
        result *= (i - 1)
        i -= 1
        
    return result
