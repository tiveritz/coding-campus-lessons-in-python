def leap_year():
    # Output all leap years from 1990 until 2040
    # Rules for leap years:
    # 1 Year number must be divisibly by four
    # 2 Not divisibly by 100
    # 3 End-of-century years must be divisible by 400

    first_year = 1800
    last_year = 2100

    for year in range(first_year, last_year+1):
        is_div_by_4 = False
        is_div_by_100 = False
        is_div_by_400 = False

        if (year % 4 == 0):
            is_div_by_4 = True
        if (year % 100 == 0):
            is_div_by_100 = True
        if (year % 400 == 0):
            is_div_by_400 = True
        
        if (is_div_by_4 and (not is_div_by_100 or is_div_by_400)):
            print(year)
