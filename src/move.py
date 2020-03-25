import check

def next(arr, char, player):
    while True:
        choice = int(input("Which field do you select " + player + " ? "))
        if check.check_move(arr, choice) == True:
            break
        else:
            print ("Issue! You have to move once more!")
    arr[choice - 1] = char
