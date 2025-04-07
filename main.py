# Importing modules ...
import random

# print(random.randint(1, 6))

def create_grid(size):
    grid = list(range(1, (size**2) + 1))
    return grid

def roll_dice():
    return random.randint(1, 6)

def check_cut_status(player, position_history, new_position):
    # getting last position ...
    last_pos_of_curr_player = new_position
    for player_ in range(len(position_history)):
        if player_ == player:
            continue
        if position_history[player_][-1] == last_pos_of_curr_player:
            position_history[player_].pop()
            position_history[player_].append(0)
    return position_history
    

def check_game_progress(last_position, roll_dice_result, grid):
    game_end_point = grid[-1]
    
    if last_position + roll_dice_result <= game_end_point:
        last_position += roll_dice_result
    return last_position
    

def start_game(grid):
    players = 3
    winner_status = False
    winner_player = None 
    position_history = [[0], [0], [0]] #{"0" : [0], "1" : [0], "2" : [0]}
    dice_role_history = [[], [], []] # {"0" : [], "1" : [], "2" : []}
    
    while not winner_status:
        for player in range(players):
            roll_dice_result = roll_dice()
            # adding dice roll result to dice_role_history
            dice_role_history[player].append(roll_dice_result)
            # getting last position ...
            last_position = position_history[player][-1]
            new_position = check_game_progress(last_position, roll_dice_result, grid)
            print(f"Player No.{player + 1} :- Roll Dice result {roll_dice_result}, Last Position :- {last_position}, New Position :- {new_position}")
            if new_position == grid[-1]:
                position_history[player].append(new_position)
                winner_status = True 
                winner_player = player
            else:
                position_history = check_cut_status(player, position_history, new_position)
                position_history[player].append(new_position)
    
    print(f"The Winner is Player {winner_player + 1}")
    
    


if __name__ == '__main__':
    n = int(input("Enter the number for Grid"))
    grid = create_grid(n)
    start_game(grid)