import re


def hello_world_string():
        # JAVA                          PYTHON
        #----------------------------------------------------
        # charAt()              ->      string[]
        # compareTo()           ->      <> <= >= ==
        # equals()              ->      ==
        # concat()              ->      string + string
        # contains()            ->      string in string
        # startsWith()          ->      startswith()
        # endsWith()            ->      endswith()
        # toLowerCase()         ->      upper()
        # toUpperCase()         ->      lower()
        # indexOf()             ->      find(), index()
        # lastIndexOf()         ->      rfind(), rindex()
        # isBlank()             ->      isspace()
        # isEmpty()             ->      not string
        # length()              ->      len()
        # replaceAll()          ->      replace(), re.sub() with regex
        # matches()             ->      re.match(), re.search()
        # strip()               ->      strip()
        # stripLeading()        ->      lstrip()
        # stripTrailing()       ->      rstrip()
        # trim()                ->

        # split()               ->      split()

        # More interesting funtions in python:
        # join() -> create strings from iterables such as lists
        # count() -> returns the number of substrings in a String
        # capitalize() -> Converts the first character of a String to upper case
        # title() -> Coverts every Word in a String to upper case

        string = "Hello World"

        print("Raw string: " + string)

        print(string[1])

        print('string == "Apfelsaft": ' + str(string == "Apfelsaft"))
        print('string <= "Zugführer": ' + str(string <= "Zugführer"))
        print('string == "Hello World": ' + str(string == "Hello World"))

        print('string.lower() == "HELLO WORLD": ' + str(string.lower() == "HELLO WORLD"))
        print('string.lower() == "hello world": ' + str(string.lower() == "hello world"))

        print('string + "!!!!!": ' + string + "!!!!!")

        print('"Apfelsaft" in string: ' + str("Apfelsaft" in string))
        print('"Worl" in string: ' + str("Worl" in string))

        print('string.startswith("Hell"): ' + str(string.startswith("Hell")))
        print('string.startswith("ld"): ' + str(string.startswith("ld")))
        print('string.endswith("Hell"): ' + str(string.endswith("Hell")))
        print('string.endswith("ld"): ' + str(string.endswith("ld")))

        print('string.upper(): ' + string.upper())
        print('string.lower(): ' + string.lower())

        # This is the old style and shouldn't be used anymore
        print("%5d" % (100))
        print("%05d" % (100))

        # New style
        print('{:>5}'.format(100))
        print('{:>05}'.format(100))

        # Difference between find() and index() is how errors are handled
        print('string.index("e"): ' + str(string.index("e")))
        print('string.index("o"): ' + str(string.index("o")))
        print('string.index("o", 6): ' + str(string.index("o", 6)))

        print('string.find("e"): ' + str(string.find("e")))
        print('string.find("o"): ' + str(string.find("o")))
        print('string.find("o", 6): ' + str(string.find("o", 6)))

        print('string.rindex("o"): ' + str(string.rindex("o")))
        print('string.rfind("o"): ' + str(string.rfind("o")))

        blanks = " "

        print('blanks.isspace(): ' + str(blanks.isspace()))
        print('not blanks: ' + str(not blanks))
        print('not "": ' + str(not ""))

        print('len(string): ' + str(len(string)))

        print('string * 3: ' + string * 3)

        print('string.replace("Hello", "Good night"): ' + string.replace("Hello", "Good night"))
        print('string.replace("World", ""): ' + string.replace("World", ""))

        textForReplace = "The resulting     pattern can then be used to create"

        print(textForReplace)
        print('textForReplace.replace(" ", "-"): ' + textForReplace.replace(" ", "-"))

        # To use regex in python the regex module has to be imported
        print('re.sub("[ ]+", " ", textForReplace: ' + re.sub("[ ]+", " ", textForReplace))
        print('re.sub("[AEIOUaeiou]", "#", textForReplace: ' + re.sub("[AEIOUaeiou]", "#", textForReplace))
        print('re.sub("[a-z]", "#", textForReplace: ' + re.sub("[a-z]", "#", textForReplace))

        deutsche_sprache = "ÄÖÜäöüß"

        replace = {
                "Ä" : "Ae",
                "ä" : "ae",
                "Ö" : "Oe",
                "ö" : "oe",
                "Ü" : "Ue",
                "ü" : "ue",
                "ß" : "ss"
        }

        for i in replace:
                deutsche_sprache = deutsche_sprache.replace(i, replace[i])

        print(deutsche_sprache)

        # Check if a given String is a valid Austrian postal code
        test_plz_1 = "1234"
        test_plz_2 = "234"
        test_plz_3 = "11234"
        test_plz_4 = "1aaa"

        pattern = re.compile('^[1-9][0-9]{3}$')

        # I prefer search instead of match, match = beginning, search = complete string
        # I define starting in the regex pattern (^...)
        print('re.search(pattern, test_plz_1): ' + str(bool(re.search(pattern, test_plz_1))))
        print('re.search(pattern, test_plz_2): ' + str(bool(re.search(pattern, test_plz_2))))
        print('re.search(pattern, test_plz_3): ' + str(bool(re.search(pattern, test_plz_3))))
        print('re.search(pattern, test_plz_4): ' + str(bool(re.search(pattern, test_plz_4))))

        print(string.split(" "))

        too_much_white_space = " Apfelsaft         "
        print(too_much_white_space)
        print('too_much_white_space.strip(): ' + "#" + too_much_white_space.strip() + "#" )
        print('too_much_white_space.lstrip(): ' + "#" + too_much_white_space.lstrip() + "#" )
        print('too_much_white_space.rstrip(): ' + "#" + too_much_white_space.rstrip() + "#" )

        print('string[4]: ' + string[4])
        print('string[4, 7]: ' + string[4:7])
        print('string[4:]: ' + string[4:])
        print('string[:4]: ' + string[:4])

def check_iban():
        test_iban_1 = "AT12 1234 1234 1234 1234"
        test_iban_2 = "AT62 6541 6985 555 0001"
        test_iban_3 = "DE55 2258 2258 2258 2211"
        test_iban_4 = "DE112 2254 2251 2251 222"

        pattern = re.compile('[A-Z]{2}[0-9]{2}(?: [0-9]{4}){4}')

        print(test_iban_1 + " is a valid postal code? " + str(bool(re.search(pattern, test_iban_1))))
        print(test_iban_2 + " is a valid postal code? " + str(bool(re.search(pattern, test_iban_2))))
        print(test_iban_3 + " is a valid postal code? " + str(bool(re.search(pattern, test_iban_3))))
        print(test_iban_4 + " is a valid postal code? " + str(bool(re.search(pattern, test_iban_4))))
