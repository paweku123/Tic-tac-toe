import os
import write
import check
import move

arr = []
for w in range(9):
    w += 1
    arr.append("%s" %w)

player1 = input("Nick 1: ")
char1 = ("X")
player2 = input("Nick 2: ")
char2 = ("0")
write.write(arr)
a = 0
while a in range(9):
    move.next(arr, char1, player1)
    write.write(arr)
    if check.check(arr, char1, player1) == True:
        break
    move.next(arr, char2, player2)
    write.write(arr)
    if check.check(arr, char2, player2) == True:
        break
    if a == 8:
        print("Remis!")
        break




