def tic_tac_toe():
    player_one = "X"
    player_two = "O"
    tic_tac_toe = create_2d_list(3, 3, " ")

    print_2d_list(tic_tac_toe)

    round = 0
    while (True):

        if round % 2 == 0:
            print("Player One ("+ player_one + ")")
            ready_player_one(tic_tac_toe, player_one)
        else:
            print("Player Two ("+ player_two + ")")
            ready_player_one(tic_tac_toe, player_two)
        
        round += 1
        print_2d_list(tic_tac_toe)

        if has_won(tic_tac_toe, player_one):
            print("Player " + player_one + " won")
            break
        elif has_won(tic_tac_toe, player_two):
            print("Player " + player_two + " won")
            break

        if is_game_field_full(tic_tac_toe):
            print("All slots full, nobody won")
            break

# ------------------------------------------------------------------------------

def create_2d_list(rows, cols, content):
    return [[content for i in range(cols)] for i in range(rows)]

def print_2d_list(game_field):
    print("-------------")
    for row in game_field:
        print("|", end = "")
        for col in row:
            print(" " + col + " |", end = "")
        print("\n-------------")

def ready_player_one(game_field, player):
    coordinates = [0,0]
    is_taken = True

    while is_taken:
        row = get_coordinate_input("Enter row: ")
        col = get_coordinate_input("Enter col: ")
        if (game_field[row][col] != " "):
            print("Already taken. Try again.")
            continue
        else:
            game_field[row][col] = player
            is_taken = False

def get_coordinate_input(message):
    coordinate = 0
    is_valid_input = False
    while not is_valid_input:
        user_input = input(message)

        if user_input.isdigit():
            coordinate = int(user_input) -1
        else:
            print("Not a valid input. Try again")
            continue
    
        if (coordinate < 0 or coordinate > 2):
            print("This is not inside the game (row 1 - 3, col 1 - 3). Try again")
            continue
        else:
            is_valid_input = True
            return coordinate

def has_won(game_field, player):
    has_won = False

    # Horizontal check
    for row in range(len(game_field)):
        if (game_field[row][0] == player and
            game_field[row][1] == player and
            game_field[row][2] == player):
            has_won = True

    # Vertical check
    for col in range(len(game_field[0])):
        if (game_field[0][col] == player and
            game_field[1][col] == player and
            game_field[2][col] == player):
            has_won = True

    # Diagonal check
    if (game_field[0][0] == player and game_field[1][1] == player and game_field[2][2] == player or
        game_field[2][0] == player and game_field[1][1] == player and game_field[0][2] == player):
        has_won = True

    return has_won

def is_game_field_full(game_field):
    is_full = True
    for row in game_field:
        for data in row:
            if data == " ":
                is_full = False
                break
    return is_full
