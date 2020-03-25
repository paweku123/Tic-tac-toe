def check_move(arr, choice):
    if arr[choice-1] != "X" and arr[choice-1] != "0":
        return True
    else:
        return False

def check(arr, char, player):
    array = [(0, 1, 2),
             (3, 4, 5),
             (6, 7, 8),
             (0, 3, 6),
             (1, 4, 7),
             (2, 5, 8),
             (0, 4, 8),
             (2, 4, 6)]

    for t in array:
        if arr[t[0]] == arr[t[1]] == arr[t[2]] == char:
            print("Player: " + player + " Win!")
            return True

    return False
