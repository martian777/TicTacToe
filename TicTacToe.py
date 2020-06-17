# write your code here
def print_row(n, state):
    state = state.replace("_", " ")
    print(f"| {state[n]} {state[n + 1]} {state[n + 2]} |")


def print_field(cells):
    print("---------")
    for i in range(0, 3):
        print_row(i * 3, cells_state)
    print("---------")


def three_in_row(symbol, row):
    if len(set(row)) == 1 and row[0] == symbol:
        return True
    return False


def check_field(field):
    xxx = False
    ooo = False
    for row in field:
        if three_in_row("X", row):
            xxx = True
        elif three_in_row("O", row):
            ooo = True
    return [xxx, ooo]


def find_state(field_h, field_v, diagonal_a, diagonal_b, cells):
    x_won_h, o_won_h = check_field(field_h)
    x_won_v, o_won_v = check_field(field_v)
    x_won_diagonal_1 = three_in_row("X", diagonal_a)
    x_won_diagonal_2 = three_in_row("X", diagonal_b)
    o_won_diagonal_1 = three_in_row("O", diagonal_a)
    o_won_diagonal_2 = three_in_row("O", diagonal_b)
    
    x_won = x_won_h or x_won_v or x_won_diagonal_1 or x_won_diagonal_2
    o_won = o_won_h or o_won_v or o_won_diagonal_1 or o_won_diagonal_2
    
    if x_won and o_won or abs(cells.count("X") - cells.count("O")) > 1:
        return "Impossible"
    elif not x_won and not o_won and "_" in cells:
        return "Game not finished"
    elif not x_won and not o_won and "_" not in cells:
        return "Draw"
    elif x_won:
        return "X wins"
    elif o_won:
        return "O wins"


def get_field_state(cells):
    matrix_h = [([e for e in cells_state[i:i + 3]]) for i in range(0, len(cells_state), 3)]
    matrix_v = [([e for e in cells_state[i::3]]) for i in range(0, 3)]
    diagonal_1 = [cells_state[x] for x in range(0, len(cells_state)) if x % 4 == 0]
    diagonal_2 = [cells_state[x] for x in range(6, 1, - 1) if x % 2 == 0]
    
    return find_state(matrix_h, matrix_v, diagonal_1, diagonal_2, cells_state)


def get_player_symbol(move_number, symbols):
    return symbols[move_number % 2]




cells_state = '_________'

print_field(cells_state)

player_symbols = ["X", "O"]
current_move_number = 0

while True:
    new_move = input("Enter the coordinates: ").split()
    valid = True
    for x in new_move:
        if not x.isdigit():
            print("You should enter numbers!")
            valid = False
            break
        elif int(x) < 1 or int(x) > 3:
            print("Coordinates should be from 1 to 3!")
            valid = False
            break
    if not valid:
        continue
    
    x, y = [(int(x) - 1) for x in new_move]
    position = (2 - y) * 3 + x
    
    if cells_state[position] != "_":
        print("This cell is occupied! Choose another one!")
        valid = False
    
    if valid:
        cells_state = [x for x in cells_state]
        cells_state[position] = get_player_symbol(current_move_number, player_symbols)
        cells_state = "".join(cells_state)
        print_field(cells_state)
        current_move_number += 1
        state = get_field_state(cells_state)
        if state != "Game not finished":
            print(state)
            break
