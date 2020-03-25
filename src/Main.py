import os

def cls():
    print ("\n" * 100)

def write(arr):
    print("%s" %arr[0] + "  |  " + "%s" %arr[1] + "  |  " + "%s" %arr[2])
    print("___|_____|__")
    print("%s" %arr[3] + "  |  " + "%s" %arr[4] + "  |  " + "%s" %arr[5])
    print("___|_____|__")
    print("%s" %arr[6] + "  |  " + "%s" %arr[7] + "  |  " + "%s" %arr[8])

def check_move(arr, choice):
    if arr[choice-1] != "X" and arr[choice-1] != "0":
        return True
    else:
        return False

def next(arr, char, player):
    while True:
        choice = int(input("Which field do you select " + player + " ? "))
        if check_move(arr, choice) == True:
            break
        else:
            print ("Issue! You have to move once more!")
    arr[choice - 1] = char

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



arr = []
for w in range(9):
    w += 1
    arr.append("%s" %w)

player1 = input("Nick 1: ")
char1 = ("X")
player2 = input("Nick 2: ")
char2 = ("0")
write(arr)
a = 0
while a in range(9):
    next(arr, char1, player1)
    write(arr)
    if check(arr, char1, player1) == True:
        break
    next(arr, char2, player2)
    write(arr)
    if check(arr, char2, player2) == True:
        break
    if a == 8:
        print("Remis!")
        break




