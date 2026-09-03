import random
import os
Position = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
Square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def Grid():
  A = Position[1] * 2
  B = Position[2] * 2
  C = Position[3] * 2
  D = Position[4] * 2
  E = Position[5] * 2
  F = Position[6] * 2
  G = Position[7] * 2
  H = Position[8] * 2
  I = Position[9] * 2
  print("Tic Tac Toe".center(50))
  print("-" * 50 + "\n")
  print(f" {A} | {B} | {C} ".center(50))
  print(f" {A} | {B} | {C} ".center(50))
  print(f"----|----|----".center(50))
  print(f" {D} | {E} | {F} ".center(50))
  print(f" {D} | {E} | {F} ".center(50))
  print(f"----|----|----".center(50))
  print(f" {G} | {H} | {I} ".center(50))
  print(f" {G} | {H} | {I} ".center(50))
def Condition():
  Count = 0
  for Index in Position:
    if Position[Index] != " ":
      Count += 1
  if Position[1] == Position[2] == Position[3] != " ":
    One, Two, Three = 1, 2, 3
  elif Position[4] == Position[5] == Position[6] != " ":
    One, Two, Three = 4, 5, 6
  elif Position[7] == Position[8] == Position[9] != " ":
    One, Two, Three = 7, 8, 9
  elif Position[1] == Position[4] == Position[7] != " ":
    One, Two, Three = 1, 4, 7
  elif Position[2] == Position[5] == Position[8] != " ":
    One, Two, Three = 2, 5, 8
  elif Position[3] == Position[6] == Position[9] != " ":
    One, Two, Three = 3, 6, 9
  elif Position[1] == Position[5] == Position[9] != " ":
    One, Two, Three = 1, 5, 9
  elif Position[3] == Position[5] == Position[7] != " ":
    One, Two, Three = 3, 5, 7
  elif Count == 9:
    return "Tie"
  else:
    One, Two, Three = 0, 0, 0
  if One != 0:
    if Position[One] == Position[Two] == Position[Three] == "O":
      return True
    elif Position[One] == Position[Two] == Position[Three] == "X":
      return False
    else:
      return None
def Winner(Result):
  os.system("clear")
  Grid()
  if Result == True:
    print("\nYou Win!")
  elif Result == False:
    print("\nYou Lose")
  elif Result == "Tie":
    print("\nTie")
Grid()
while True:
  Player_Move = int(input("\nChoose Your Move (1-9): "))
  while True:
    if Player_Move in Square:
      Position[Player_Move] = "O"
      Square.remove(Player_Move)
      break
    elif Player_Move < 1 or Player_Move > 9:
      Player_Move = int(input("Please enter a number between 1 and 9: "))
    else:
      Player_Move = int(input("Please choose a square that is not taken: "))
  Result = Condition()
  if Result != None:
    Winner(Result)
    break
  Winner(Result)
  AI_Move = random.choice(Square)
  Square.remove(AI_Move)
  Position[AI_Move] = "X"
  Result = Condition()
  if Result != None:
    Winner(Result)
    break
  os.system("clear")
  Grid()
