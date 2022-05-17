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
bord = (''' 
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
marks_table = ["X", "x", "O", "o"]


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

      print(player_1)
      print(player_2)
      
      print

      #wybór kto używa kółka, kto krzyżyka
      #print(str(player_1), + ", please chose your mark (for X type just x, for O type just o like open.")
      #player_1_sign = input()









#jeżeli multi player to musi być jasno określone kto ma X a kto ma O i musi to być zrobione drogą losowania
#musi być też wybór random kto zaczyna grę
#if type_game == "1":
      #print("Please choose your sign: X or O.")
      #player_A_sign = input("Your choice is: ")
      #print(player_A_sign)
      
#game_table = [ [ 'A1','A2','A3' ],[ 'B1','B2','B3' ],[ 'C1','C2','C3' ] ]
#game_table_dots = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
#print(game_table)





#players_table = [player_A, player_B]

#elif type_game == "2":
     # import random
      #player_1 = random.choice(players_table)
     # if player_1 == player_A:
            #player_2 = player_B
      #else:
           # player_2 = player_A

#print(player_1)
#print(player_2)
