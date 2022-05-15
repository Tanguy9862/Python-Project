table = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def show_table():
    for line in table:
        print(line)
        
def place_marker(marker):
    if table[int(user_choice[0])-1][int(user_choice[1])-1] == "-":
        table[int(user_choice[0])-1][int(user_choice[1])-1] = marker

def check_empty():
    if table[int(user_choice[0])-1][int(user_choice[1])-1] == "O" or table[int(user_choice[0])-1][int(user_choice[1])-1] == "X":
        return False
    else:
        return True

def check_for_winner():
    # Check horizontal:
    for i in range(len(table)):
        if all(element == table[i][0] for element in table[i]) and '-' not in table[i]:
            return True

    # Check vertical: 
    for i in range(len(table)):
        if table[0][i] == table[1][i] and table[1][i] == table[2][i] and table[0][i] != '-':
            return True
        
    # Check diagnoal:
    if table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][1] != '-':
        return True
    elif table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2] != '-':
        return True
    return False
    
n = 0
while True:
    show_table()
    user_choice = input("Choose your position for your marker (Line:Column) : ").split(':')
    
    if check_empty():
        if n % 2 == 0:
            marker = "O"
            place_marker(marker=marker)
        else:
            marker = "X"
            place_marker(marker=marker)
        n += 1
        if check_for_winner():
            show_table()
            print(f"{marker} win the game!")
            break
    else:
        print("There is already a marker here, please choose another place!")
