import re


def string_repetition():
    my_sentence = "Das sit ein Satz. Einmal mehr sage ich eines zu euch. Ein Mensch hat Hände."

    #1 Count character "."
    char_count = 0
    for character in my_sentence:
        if character == ".":
            char_count += 1
    
    print('Amount of ".": ' + str(char_count))

    #2 Count occurence of "Hand"
    sentence_full_of_hands = ("Das ist eine Hand. Mit der Hand kann ich winken. "
                              + "Freundlichen Menschen gebe ich gerne die Hand. "
                              + "Im Winter trage ich Handschuhe."
                              + "Gibst du mir deine Hand?")
    
    normalized = sentence_full_of_hands.replace(".", " ").replace("?", " ").replace("  ", " ")
    words = normalized.split(" ")

    word_count = 0

    for word in words:
        if word == "Hand":
            word_count += 1
    
    print('Number of "Hand": ' + str(word_count))

    # Repetition 1 with another sentence
    sentence_winter = "ImWinter;trage_ich Handschuhe."
    sentence_winter_normalized = sentence_winter.replace(".", "") #easy workaround
    sentence_winter_normalized = re.sub("[;_]", " ", sentence_winter_normalized)
    sentence_winter_normalized = re.sub("(?<=[a-z])(?=[A-Z])", " ", sentence_winter_normalized)

    print("Clean sentence: " + sentence_winter)
    print("Clean sentence: " + sentence_winter_normalized)

    #2 Detect words
    words = sentence_winter_normalized.split(" ")
    print(words)

    print("Amount of words: " + str(len(words)))
