def list_to_string():
        # Gib ein Array mit print aus. Dann reprodizier die
        # Ausgabe 1:1 mit eigenem Code

    my_list = [1, 2, 3, 99]
    print(my_list)

    output = "["
    i = 0
    for element in my_list:
        output = output + str(element)
        if i < len(my_list)-1:
            output += ", "
        i += 1
    output += "]"

    print(output)

# ----------------------------------------------------------------------

def index_to_month(index):
    index_month_mapping = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November",
                      "December"]
    return(index_month_mapping[index])

def business_result():
    # Ein Buchladen hat den folgenden Montastergebnisse:
    business_result = [1, 2, -5, 3, 10, -2, -1, -3, 0, 3, 6, 7]
    print(business_result)

    # 1 Was ist das Gesamtergebnis? (Summe der Monatsergebnisse)
    total_result = 0
    for month in business_result:
        total_result += month
    
    print("The total result is " + str(total_result))

    # 2 Was ist das beste Monatsergebnis?
    # 3 In welchem Monat war das beste Monatsergebnis?
    i = 0
    best_result = business_result[0]
    best_result_index = 0
    for month in business_result:
        if (month > best_result):
            best_result = month
            best_result_index = i
        i += 1
    
    best_result_month = index_to_month(best_result_index)

    print("The best result is " + str(best_result))
    print("The best result is in " + best_result_month)

    # 4 Was ist das schwächste Monatsergebnis?
    # 5 In welchem Monat war das schwächste Monatsergebnis?
    i = 0
    worst_result = business_result[0]
    worst_result_index = 0
    for month in business_result:
        if (month < worst_result):
            worst_result = month
            worst_result_index = i
        i += 1
    
    worst_result_month = index_to_month(worst_result_index)

    print("The worst result is " + str(worst_result))
    print("The worst result is in " + worst_result_month)

    # 6 War zwei hintereinander kommende Monate mit negativen Ergebnis?
    has_two_neg_month_row = False

    i = 0
    for month in range(len(business_result) - 1):
        if (business_result[i] < 0 and business_result[i + 1] < 0 ):
            has_two_neg_month_row = True
            break
        i += 1

    if has_two_neg_month_row:
        print("Yes, two bad month in a row")
    else:
        print("No, no two bad month in a row")

    # 7 Was war das längste Intervall mit negativen Ergebnis?
    counter = 0
    max_neg = 0

    for i in range(len(business_result)):
        if (business_result[i] < 0):
            counter += 1
            if (counter > max_neg):
                max_neg = counter
        else:
            counter = 0
        i +=i
    
    print("Longest negative period is " + str(max_neg) + " months")

    # 8 Was war das zweitbeste Ergebnis?
    second_best_result = worst_result

    for i in range(len(business_result)):
        if (business_result[i] > second_best_result and business_result[i] < best_result):
            second_best_result = business_result[i]
        i += 1

    print("Second best result is " + str(second_best_result))
