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
    if arr[0] == arr[1] == arr[2] == char or arr[3] == arr[4] == arr[5] == char or arr[6] == arr[7] == arr[8] == char or arr[0] == arr[3] == arr[6] == char or arr[1] == arr[4] == arr[7] == char or arr[2] == arr[5] == arr[8] == char or arr[0] == arr[4] == arr[8] == char or arr[2] == arr[4] == arr[6] == char:
        print("Player: " + player + " Win!")
        return True
    else:
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




