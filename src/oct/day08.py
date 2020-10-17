def sort_names_list():
    names = [
            "Austrian",
            "KLM",
            "China",
            "Ryan Air",
            "Lufthansa",
            "United",
            "American",
            "Turkish",
            "Aeromexico",
            "Alitalia",
            "Delta",
            "Quatar",
            "Austrian",
            #"Äustrian",
            "Quatar",
            ]
    
    # 1. Wie viele Elemente sind in der Liste?
    print("1 Elements in array: " + str(len(names)))

    # 2.1 Was ist das kürzeste Element? (Pos + Name)
    shortest_elem = names[0]
    shortest_elem_index = 0

    i = 0
    for name in names:
        if (len(shortest_elem) > len(name)):
            shortest_elem = name
            shortest_elem_index = i
        i += 1

    print("2.1 Shortest Element: " + shortest_elem +
          " at index " + str(shortest_elem_index))

    # 2.2. Was ist das längste Element? (Pos + Name)
    longest_elem = names[0]
    longest_elem_index = 0

    i = 0
    for name in names:
        if (len(longest_elem) < len(name)):
            longest_elem = name
            longest_elem_index = i
        i += 1

    print("2.2 Longest Element: " + longest_elem +
          " at index " + str(longest_elem_index))
    
    # 3.1. Was ist alphabetisch das erste Element? (Pos + Name)
    abc_first_elem = names[0]
    abc_first_elem_index = 0

    i = 0
    for name in names:
        if(abc_first_elem > name):
            abc_first_elem = name
            abc_first_elem_index = i
        i += 1
    
    print("3.1 Alphabetically first Element: " + abc_first_elem +
          " at index " + str(abc_first_elem_index))
    
    # 3.2. Was ist alphabetisch das letzte Element? (Pos + Name)
    abc_last_elem = names[0]
    abc_last_elem_index = 0

    i = 0
    for name in names:
        if(abc_last_elem < name):
            abc_last_elem = name
            abc_last_elem_index = i
        i += 1
    
    print("3.2 Alphabetically last Element: " + abc_last_elem +
          " at index " + str(abc_last_elem_index))
    
    # 4.1. Gibt es ein Element 2 Mal?
    duplicate = False

    for i in range(len(names)):
        for j in range(len(names)):
            if (i == j):
                continue
            elif (names[i] == names[j]):
                duplicate = True
            j += 1
        i += 1

        if duplicate:
            break

    if duplicate:
        print("4.1 There is at least one duplicate")
    else:
        print("4.1 There are no duplicates")
    
    # 4.2. Welche Elemente gibt es doppelt?
    for i in range(len(names)):
        for j in range(len(names)):
            if (i == j):
                continue
            elif (names[i] == names[j]):
                print("4.1 Duplicate found: " + names[i])
            j += 1
        i += 1

    # 8. Sortiere alphabetisch absteigend.
    names_sort = names

    for i in range(len(names)):
        for j in range(len(names) - 1 - i):
            if (names_sort[j] < names_sort[j + 1]):
                names_sort[j], names_sort[j + 1] = names_sort [j + 1], names_sort[j]
            j += 1
        i += 1

    print(names_sort)

    # Zusatzaufgabe
    # Primäre Sortierung nach Elementlänge absteigend
    # Secundäre Sortierung alphabetisch aufsteigend
    names_double_sort = names

    for i in range(len(names)):
        for j in range(len(names) - 1 - i):
            if (len(names_double_sort[j]) <= len(names_double_sort[j + 1])):
                if (names_double_sort[j] > names_double_sort[j + 1]):
                    names_double_sort[j], names_double_sort[j + 1] = names_double_sort [j + 1], names_double_sort[j]
            j += 1
        i += 1
    
    print(names_double_sort)
