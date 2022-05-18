from ast import Break
from tracemalloc import stop

print()
#powitanie  
print("Hello! Welcome in Tic Tac Toe Game. Before starting, please choose type of the game:")
print("- single player / against computer (type: 1))")

#wybór single palyer i mulit player
print("- multiplayer (type: 2)")
type_game = input("Your choice is: ")
valid_type_game = ["1", "2"]

while not type_game in valid_type_game:
    print("Please choose the type game correctly only from: 1 or 2.")
    type_game = input("Your choice is: ")

#pobranie imienia / imion graczy
else:
    if type_game == "1": 
        
        player_A = input("Please give your name: ")
        print(f"Okay... Let's fight " + str(player_A) + " with the computer!")
    else:
        print("Let's play together with your friend!")
        player_A = str(input("Please give the name of the first player: "))
        player_B = str(input("Please give the name of the second player: "))
        


#tablica kółko i krzyżyk w systemie ACII
board_ASCI = (''' 
   A     B     C
      |     |     
1  .  |  .  |  .  
 _____|_____|_____
      |     |     
2  .  |  .  |  .  
 _____|_____|_____
      |     |     
3  .  |  .  |  .  
      |     |  ''')

#tablica do grania
board_0_work = [" ", "A", "|", "B", "|", "C"]
board_1_work = ["1", "A1", "|", "B1", "|", "C1"]
board_2_work = ["2", "A2", "|", "B2", "|", "C2"]
board_3_work = ["3", "A3", "|", "B3", "|", "C3"]

board_0 = [" ", "A", "|", "B", "|", "C"]
board_1 = ["1", ".", "|", ".", "|", "."]
board_2 = ["2", ".", "|", ".", "|", "."]
board_3 = ["3", ".", "|", ".", "|", "."]

#rozwiązania, które dają wygraną graczowi
#board_1_work[1] == board_2_work[1] == board_3_work[1]
#board_1_work[3] == board_2_work[3] == board_3_work[3]
#board_1_work[5] == board_2_work[5] == board_3_work[5]
#board_1_work[1] == board_1_work[3] == board_1_work[5]
#board_2_work[1] == board_2_work[3] == board_2_work[5]
#board_3_work[1] == board_3_work[3] == board_3_work[5]
#board_1_work[1] == board_2_work[3] == board_3_work[5]
#board_3_work[1] == board_2_work[3] == board_1_work[5]

#tablica znaków do grania
marks_table = ["X", "O",]
winner = []


print()

#rozpiska dla wersji multiplayer
if type_game == "2":
      #wybór kto jest graczem nr 1 a kto graczem nr 2
      players_table = [player_A, player_B]
      player_1 = input("Who is going to start the game? " + str(player_A) + " or " + str(player_B) + "?: ")\
      
      while not player_1 in players_table:
            print(f"Please give the correct name of the first player. You can choose from: ", player_A, " and ", player_B, ".", sep="")
            player_1 = input("The first player is: ")
      else:
            pass

      if player_1 == player_A:
          player_2 = player_B
      else:
          player_2 = player_A

      print(f"{player_1} --> Player nr 1")
      print(f"{player_2} --> Player nr 2")
      
      
      print()
      print(f"Ok {player_1}, now please choose what is your mark. For X type x like xerox and for O type o like open.")
      player_1_mark = str(input("Your mark is: "))
      player_1_mark_up = str.upper(player_1_mark)
    


      while not player_1_mark_up in marks_table:
          print("Please provide correct mark: X or O (you can use lowercase too).")
          player_1_mark = str(input("Your mark is: "))
          player_1_mark_up = str.upper(player_1_mark)
      else:
          if player_1_mark_up == "X":
              player_2_mark_up = "O"
          else:
              player_2_mark_up = "X"
      

      print(f"{player_1} --> {player_1_mark_up}")
      print(f"{player_2} --> {player_2_mark_up}")
      print()
      
      print(f"Ok guys, this is the board game. Please type the cell address, where you want to sign your mark (for example please type: A2 or b2).")
      

      
      # pierwsze 4 ruchy na tablicy
      for i in range(2):
          print()
          print(*board_0)
          print(*board_1)
          print(*board_2)
          print(*board_3)
          print()
          print(f"{player_1} your move!")
          player_1_position = input("Please type your position: ")
          player_1_position_upper = player_1_position.upper()
          if player_1_position_upper == "A1" and board_1_work[1] == "A1":
              board_1[1] = player_1_mark_up
              board_1_work[1] = player_1_mark_up
          elif player_1_position_upper == "A2" and board_2_work[1] == "A2":
              board_2[1] = player_1_mark_up
              board_2_work[1] = player_1_mark_up
          elif player_1_position_upper == "A3" and board_3_work[1] == "A3":
              board_3[1] = player_1_mark_up
              board_3_work[1] = player_1_mark_up
          elif player_1_position_upper == "B1" and board_1_work[3] == "B1":
              board_1[3] = player_1_mark_up
              board_1_work[3] = player_1_mark_up
          elif player_1_position_upper == "B2" and board_2_work[3] == "B2":
              board_2[3] = player_1_mark_up
              board_2_work[3] = player_1_mark_up
          elif player_1_position_upper == "B3" and board_3_work[3] == "B3":
              board_3[3] = player_1_mark_up
              board_3_work[3] = player_1_mark_up
          elif player_1_position_upper == "C1" and board_1_work[5] == "C1":
              board_1[5] = player_1_mark_up
              board_1_work[5] = player_1_mark_up
          elif player_1_position_upper == "C2" and board_2_work[5] == "C2":
              board_2[5] = player_1_mark_up
              board_2_work[5] = player_1_mark_up
          elif player_1_position_upper == "C3" and board_3_work[5] == "C3":
              board_3[5] = player_1_mark_up
              board_3_work[5] = player_1_mark_up
          print()
          print(*board_0)
          print(*board_1)
          print(*board_2)
          print(*board_3)
          print()

          print(f"{player_2} your move!")
          player_2_position = input("Please type your position: ")
          player_2_position_upper = player_2_position.upper()
          if player_2_position_upper == "A1" and board_1_work[1] == "A1":
              board_1[1] = player_2_mark_up
              board_1_work[1] = player_2_mark_up
          elif player_2_position_upper == "A2" and board_2_work[1] == "A2":
              board_2[1] = player_2_mark_up
              board_2_work[1] = player_2_mark_up
          elif player_2_position_upper == "A3" and board_3_work[1] == "A3":
              board_3[1] = player_2_mark_up
              board_3_work[1] = player_2_mark_up
          elif player_2_position_upper == "B1" and board_1_work[3] == "B1":
              board_1[3] = player_2_mark_up
              board_1_work[3] = player_2_mark_up
          elif player_2_position_upper == "B2" and board_2_work[3] == "B2":
              board_2[3] = player_2_mark_up
              board_2_work[3] = player_2_mark_up
          elif player_2_position_upper == "B3" and board_3_work[3] == "B3":
              board_3[3] = player_2_mark_up
              board_3_work[3] = player_2_mark_up
          elif player_2_position_upper == "C1" and board_1_work[5] == "C1":
              board_1[5] = player_2_mark_up
              board_1_work[5] = player_2_mark_up
          elif player_2_position_upper == "C2" and board_2_work[5] == "C2":
              board_2[5] = player_2_mark_up
              board_2_work[5] = player_2_mark_up
          elif player_2_position_upper == "C3" and board_3_work[5] == "C3":
              board_3[5] = player_2_mark_up
              board_3_work[5] = player_2_mark_up

      print()
      print(*board_0)
      print(*board_1)
      print(*board_2)
      print(*board_3)
      print()
      # 5. ruch na tablicy
      print(f"{player_1} your move!")
      player_1_position = input("Please type your position: ")
      player_1_position_upper = player_1_position.upper()
      if player_1_position_upper == "A1" and board_1_work[1] == "A1":
          board_1[1] = player_1_mark_up
          board_1_work[1] = player_1_mark_up
      elif player_1_position_upper == "A2" and board_2_work[1] == "A2":
          board_2[1] = player_1_mark_up
          board_2_work[1] = player_1_mark_up
      elif player_1_position_upper == "A3" and board_3_work[1] == "A3":
          board_3[1] = player_1_mark_up
          board_3_work[1] = player_1_mark_up
      elif player_1_position_upper == "B1" and board_1_work[3] == "B1":
          board_1[3] = player_1_mark_up
          board_1_work[3] = player_1_mark_up
      elif player_1_position_upper == "B2" and board_2_work[3] == "B2":
           board_2[3] = player_1_mark_up
           board_2_work[3] = player_1_mark_up
      elif player_1_position_upper == "B3" and board_3_work[3] == "B3":
           board_3[3] = player_1_mark_up
           board_3_work[3] = player_1_mark_up
      elif player_1_position_upper == "C1" and board_1_work[5] == "C1":
           board_1[5] = player_1_mark_up
           board_1_work[5] = player_1_mark_up
      elif player_1_position_upper == "C2" and board_2_work[5] == "C2":
           board_2[5] = player_1_mark_up
           board_2_work[5] = player_1_mark_up
      elif player_1_position_upper == "C3" and board_3_work[5] == "C3":
           board_3[5] = player_1_mark_up
           board_3_work[5] = player_1_mark_up
    
      print()
      print(*board_0)
      print(*board_1)
      print(*board_2)
      print(*board_3)
      print()

      # sprawdzenie po 5. ruchu
      while board_1_work[3] == board_2_work[3] == board_3_work[3] or board_1_work[1] == board_2_work[1] == board_3_work[1] or board_1_work[5] == board_2_work[5] == board_3_work[5] or board_1_work[1] == board_1_work[3] == board_1_work[5] or board_2_work[1] == board_2_work[3] == board_2_work[5] or board_3_work[1] == board_3_work[3] == board_3_work[5] or board_1_work[1] == board_2_work[3] == board_3_work[5] or board_3_work[1] == board_2_work[3] == board_1_work[5]:
          
          print(f"Congratulations!!! The winner is {player_1}!")
          print()
          break
      #wprowadzenie 6 znaku
      else:
          print()
          print(*board_0)
          print(*board_1)
          print(*board_2)
          print(*board_3)
          print()
          print(f"{player_2} your move!")
          player_2_position = input("Please type your position: ")
          player_2_position_upper = player_2_position.upper()
          if player_2_position_upper == "A1" and board_1_work[1] == "A1":
              board_1[1] = player_2_mark_up
              board_1_work[1] = player_2_mark_up
          elif player_2_position_upper == "A2" and board_2_work[1] == "A2":
              board_2[1] = player_2_mark_up
              board_2_work[1] = player_2_mark_up
          elif player_2_position_upper == "A3" and board_3_work[1] == "A3":
              board_3[1] = player_2_mark_up
              board_3_work[1] = player_2_mark_up
          elif player_2_position_upper == "B1" and board_1_work[3] == "B1":
              board_1[3] = player_2_mark_up
              board_1_work[3] = player_2_mark_up
          elif player_2_position_upper == "B2" and board_2_work[3] == "B2":
              board_2[3] = player_2_mark_up
              board_2_work[3] = player_2_mark_up
          elif player_2_position_upper == "B3" and board_3_work[3] == "B3":
              board_3[3] = player_2_mark_up
              board_3_work[3] = player_2_mark_up
          elif player_2_position_upper == "C1" and board_1_work[5] == "C1":
              board_1[5] = player_2_mark_up
              board_1_work[5] = player_2_mark_up
          elif player_2_position_upper == "C2" and board_2_work[5] == "C2":
              board_2[5] = player_2_mark_up
              board_2_work[5] = player_2_mark_up
          elif player_2_position_upper == "C3" and board_3_work[5] == "C3":
              board_3[5] = player_2_mark_up
              board_3_work[5] = player_2_mark_up
          
          #sprawdzenie po 6 znaku
          while board_1_work[3] == board_2_work[3] == board_3_work[3] or board_1_work[1] == board_2_work[1] == board_3_work[1] or board_1_work[5] == board_2_work[5] == board_3_work[5] or board_1_work[1] == board_1_work[3] == board_1_work[5] or board_2_work[1] == board_2_work[3] == board_2_work[5] or board_3_work[1] == board_3_work[3] == board_3_work[5] or board_1_work[1] == board_2_work[3] == board_3_work[5] or board_3_work[1] == board_2_work[3] == board_1_work[5]:
               print()
               print(*board_0)
               print(*board_1)
               print(*board_2)
               print(*board_3)
               print()
               print(f"Congratulations!!! The winner is {player_2}!")
               print()
               break
          
          #wprowadzenie 7 znaku
          else:
              print()
              print(*board_0)
              print(*board_1)
              print(*board_2)
              print(*board_3)
              print()
              print(f"{player_1} your move!")
              player_1_position = input("Please type your position: ")
              player_1_position_upper = player_1_position.upper()
              if player_1_position_upper == "A1" and board_1_work[1] == "A1":
                  board_1[1] = player_1_mark_up
                  board_1_work[1] = player_1_mark_up
              elif player_1_position_upper == "A2" and board_2_work[1] == "A2":
                  board_2[1] = player_1_mark_up
                  board_2_work[1] = player_1_mark_up
              elif player_1_position_upper == "A3" and board_3_work[1] == "A3":
                  board_3[1] = player_1_mark_up
                  board_3_work[1] = player_1_mark_up
              elif player_1_position_upper == "B1" and board_1_work[3] == "B1":
                  board_1[3] = player_1_mark_up
                  board_1_work[3] = player_1_mark_up
              elif player_1_position_upper == "B2" and board_2_work[3] == "B2":
                  board_2[3] = player_1_mark_up
                  board_2_work[3] = player_1_mark_up
              elif player_1_position_upper == "B3" and board_3_work[3] == "B3":
                  board_3[3] = player_1_mark_up
                  board_3_work[3] = player_1_mark_up
              elif player_1_position_upper == "C1" and board_1_work[5] == "C1":
                  board_1[5] = player_1_mark_up
                  board_1_work[5] = player_1_mark_up
              elif player_1_position_upper == "C2" and board_2_work[5] == "C2":
                  board_2[5] = player_1_mark_up
                  board_2_work[5] = player_1_mark_up
              elif player_1_position_upper == "C3" and board_3_work[5] == "C3":
                  board_3[5] = player_1_mark_up
                  board_3_work[5] = player_1_mark_up
              
              #sprawdzenie po 7 znaku
              while board_1_work[3] == board_2_work[3] == board_3_work[3] or board_1_work[1] == board_2_work[1] == board_3_work[1] or board_1_work[5] == board_2_work[5] == board_3_work[5] or board_1_work[1] == board_1_work[3] == board_1_work[5] or board_2_work[1] == board_2_work[3] == board_2_work[5] or board_3_work[1] == board_3_work[3] == board_3_work[5] or board_1_work[1] == board_2_work[3] == board_3_work[5] or board_3_work[1] == board_2_work[3] == board_1_work[5]:
                  print()
                  print(*board_0)
                  print(*board_1)
                  print(*board_2)
                  print(*board_3)
                  print()
                  print(f"Congratulations!!! The winner is {player_1}!")
                  print()
                  break
              #wprowadzenie 8 znaku
              else:
                  print()
                  print(*board_0)
                  print(*board_1)
                  print(*board_2)
                  print(*board_3)
                  print()
                  print(f"{player_2} your move!")
                  player_2_position = input("Please type your position: ")
                  player_2_position_upper = player_2_position.upper()
                  if player_2_position_upper == "A1" and board_1_work[1] == "A1":
                      board_1[1] = player_2_mark_up
                      board_1_work[1] = player_2_mark_up
                  elif player_2_position_upper == "A2" and board_2_work[1] == "A2":
                      board_2[1] = player_2_mark_up
                      board_2_work[1] = player_2_mark_up
                  elif player_2_position_upper == "A3" and board_3_work[1] == "A3":
                      board_3[1] = player_2_mark_up
                      board_3_work[1] = player_2_mark_up
                  elif player_2_position_upper == "B1" and board_1_work[3] == "B1":
                      board_1[3] = player_2_mark_up
                      board_1_work[3] = player_2_mark_up
                  elif player_2_position_upper == "B2" and board_2_work[3] == "B2":
                      board_2[3] = player_2_mark_up
                      board_2_work[3] = player_2_mark_up
                  elif player_2_position_upper == "B3" and board_3_work[3] == "B3":
                      board_3[3] = player_2_mark_up
                      board_3_work[3] = player_2_mark_up
                  elif player_2_position_upper == "C1" and board_1_work[5] == "C1":
                      board_1[5] = player_2_mark_up
                      board_1_work[5] = player_2_mark_up
                  elif player_2_position_upper == "C2" and board_2_work[5] == "C2":
                      board_2[5] = player_2_mark_up
                      board_2_work[5] = player_2_mark_up
                  elif player_2_position_upper == "C3" and board_3_work[5] == "C3":
                      board_3[5] = player_2_mark_up
                      board_3_work[5] = player_2_mark_up
                
                #sprawdzenie po 8 znaku
                  while board_1_work[3] == board_2_work[3] == board_3_work[3] or board_1_work[1] == board_2_work[1] == board_3_work[1] or board_1_work[5] == board_2_work[5] == board_3_work[5] or board_1_work[1] == board_1_work[3] == board_1_work[5] or board_2_work[1] == board_2_work[3] == board_2_work[5] or board_3_work[1] == board_3_work[3] == board_3_work[5] or board_1_work[1] == board_2_work[3] == board_3_work[5] or board_3_work[1] == board_2_work[3] == board_1_work[5]:
                      print()
                      print(*board_0)
                      print(*board_1)
                      print(*board_2)
                      print(*board_3)
                      print()
                      print(f"Congratulations!!! The winner is {player_2}!")
                      print()
                      break
                  else:
                      print()
                      print(*board_0)
                      print(*board_1)
                      print(*board_2)
                      print(*board_3)
                      print()
                      print(f"{player_1} your move!")
                      player_1_position = input("Please type your position: ")
                      player_1_position_upper = player_1_position.upper()
                      if player_1_position_upper == "A1" and board_1_work[1] == "A1":
                          board_1[1] = player_1_mark_up
                          board_1_work[1] = player_1_mark_up
                      elif player_1_position_upper == "A2" and board_2_work[1] == "A2":
                          board_2[1] = player_1_mark_up
                          board_2_work[1] = player_1_mark_up
                      elif player_1_position_upper == "A3" and board_3_work[1] == "A3":
                          board_3[1] = player_1_mark_up
                          board_3_work[1] = player_1_mark_up
                      elif player_1_position_upper == "B1" and board_1_work[3] == "B1":
                          board_1[3] = player_1_mark_up
                          board_1_work[3] = player_1_mark_up
                      elif player_1_position_upper == "B2" and board_2_work[3] == "B2":
                          board_2[3] = player_1_mark_up
                          board_2_work[3] = player_1_mark_up
                      elif player_1_position_upper == "B3" and board_3_work[3] == "B3":
                          board_3[3] = player_1_mark_up
                          board_3_work[3] = player_1_mark_up
                      elif player_1_position_upper == "C1" and board_1_work[5] == "C1":
                          board_1[5] = player_1_mark_up
                          board_1_work[5] = player_1_mark_up
                      elif player_1_position_upper == "C2" and board_2_work[5] == "C2":
                          board_2[5] = player_1_mark_up
                          board_2_work[5] = player_1_mark_up
                      elif player_1_position_upper == "C3" and board_3_work[5] == "C3":
                          board_3[5] = player_1_mark_up
                          board_3_work[5] = player_1_mark_up
                    
                    #sprawdzenie po 9 znaku
                      while board_1_work[3] == board_2_work[3] == board_3_work[3] or board_1_work[1] == board_2_work[1] == board_3_work[1] or board_1_work[5] == board_2_work[5] == board_3_work[5] or board_1_work[1] == board_1_work[3] == board_1_work[5] or board_2_work[1] == board_2_work[3] == board_2_work[5] or board_3_work[1] == board_3_work[3] == board_3_work[5] or board_1_work[1] == board_2_work[3] == board_3_work[5] or board_3_work[1] == board_2_work[3] == board_1_work[5]:
                          print()
                          print(*board_0)
                          print(*board_1)
                          print(*board_2)
                          print(*board_3)
                          print()
                          print(f"Congratulations!!! The winner is {player_1}!")
                          print()
                          break
                      else:
                          print()
                          print("The game is end. There is no the winner!")
                          print()
