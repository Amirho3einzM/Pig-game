import random

def roll():
    max_value = 6
    min_value = 1
    x = 0
    z = 0
    w = 0
    f_roll = random.randint(min_value, max_value)
    s_roll = random.randint(min_value, max_value)
    if f_roll == s_roll:
        x = 1
    if s_roll == 1 or f_roll == 1:
        z = 1
    if s_roll == 1 and f_roll == 1:
        w = 1
    
    return x, z, w, f_roll, s_roll

while True:
    players = input("\nHow many people want to play (2 to 4):\n...")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("\nPlease choose between 2 to 4.\n")
    else:
        print("\nPlease use numbers only.\n")

while True:
    top_score=input("\nEnter Top Score (10 to 100)\n... ")
    if top_score.isdigit():
        top_score=int(top_score)
        if 10<=top_score<=100:
            break
        else:
            
            print("\nPlease choose between 10 to 100.\n")
    else:
        print("\nPlease use numbers only.\n")
            
        
players_score = [0 for _ in range(players)]

game_over = False

while not game_over:
    for player_num in range(players):
        continue_turn = True
        while continue_turn:
            for index, score in enumerate(players_score):
                print("player {0} : {1}".format(index+1,score))
            print("\nIt's player {0}'s turn.\n".format(player_num + 1))
            print("\nYour score is {0}.\n".format(players_score[player_num]))
            roll_again = 0
            current_score = 0
            
            answer2 = input("Do you want to roll? (y/n)").lower()
            
            if answer2 != "y":
                break
            else:
                x, z, w, f_roll, s_roll = roll()
                result = (f_roll) + (s_roll)
                if w!=1:
                    current_score = result
                print("\nYou roll {0} and {1} \n".format(f_roll, s_roll))
                
                if s_roll!=f_roll:
                    continue_turn = False
                    
                if w == 1:
                    print("\nYou rolled two 1s. Each player gets 1 point!\n")
                    for i in range(players):
                        players_score[i] += 1
                    continue_turn = False
                    
                elif x == 1:
                    print("\nYou can roll again!\n")
                    # players_score[player_num] += current_score
                    
                elif z == 1:
                    print("\nYou rolled a 1. Your score remains 0!\n")
                    players_score[player_num] = 0
                    current_score = 0
                    continue_turn = False
            if w!=1:        
                players_score[player_num] += current_score
            if max(players_score) >= top_score:
                game_over = True
                break
    if game_over:
        break

print("Player {0} wins with a score of {1}.".format(players_score.index(max(players_score)) + 1, max(players_score)))
