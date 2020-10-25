import random

def random_array_print():
    shortcut = ["lol", "hdl", "mfg", "rofl", "asdf"]
    emoji = [":-)", "<3", ":|", ":P"]

    for i in range(5):
        rand_inex_shortcut = random.randint(0, len(shortcut)-1)
        rand_index_emoji = random.randint(0, len(emoji)-1)
        print(shortcut[rand_inex_shortcut] + " " + emoji[rand_index_emoji])
