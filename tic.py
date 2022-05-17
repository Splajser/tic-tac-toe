from prettytable import PrettyTable
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



#tablica znaków do grania
marks_table = ["X", "O",]


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
      player_1_mark = input("Your mark is: ")
      player_1_mark_up = str.upper(player_1_mark)
      


      while not player_1_mark_up in marks_table:
          print("Please provide correct mark: X or O (you can use lowercase too).")
          player_1_mark = input("Your mark is: ")
          player_1_mark_up = str.upper(player_1_mark)
      else:
          if player_1_mark_up == "X":
              player_2_mark_up = "O"
          else:
              player_2_mark_up = "X"
      

      print(f"{player_1} --> {player_1_mark_up}")
      print(f"{player_2} --> {player_2_mark_up}")
      print()
      
      print(f"Ok guys, this is the board game. To start, {player_1} please type the cell address, where you want to sign your mark (for example please type: A2 or b2).")
      print(board_ASCI)
      print()

      mydata = [
          ["Nikhil", "Delhi"],
          ["Ravi", "Kanpur"],
          ["Manish", "Ahmedabad"],
          ["Prince", "Bangalore"]
      ]
      head = ["Name", "City"]
      print(mydata)
      print(tabulate(mydata, headers=head, tablefmt="grid"))
