from input_helper import convert_data_to_list


OPPONENT_GUIDE = {"A": ["Rock", 1],
                  "B": ["Paper", 2],
                  "C": ["Scissors", 3]}

STRATEGY_GUIDE = {"X": ["Rock", 1],
                  "Y": ["Paper", 2],
                  "Z": ["Scissors", 3]}

OUTCOMES_GUIDE = {"X": ["Lose", 0],
                  "Y": ["Draw", 3],
                  "Z": ["Win", 6]}

OPP_TO_YOU_LOSING_GAMES = {(3, 2), (2, 1), (1, 3)}
OPP_TO_YOU_WINNING_GAMES = {(3, 1), (2, 3), (1, 2)}


########### PART 1 ###########
def your_total_score_strategy_1(file_name):
    your_score = 0
    
    rounds = convert_data_to_list(file_name)
    for round in rounds:
        opponent_move = OPPONENT_GUIDE[round[0]][1]
        your_move = STRATEGY_GUIDE[round[2]][1]

        your_score += your_move
        
        if your_move == opponent_move:
            your_score += 3
        elif (opponent_move, your_move) in OPP_TO_YOU_WINNING_GAMES:
            your_score += 6

    return your_score
    
########### PART 2 ###########
def your_move(outcome, opponent_move):
    if outcome == 0:
        for game in OPP_TO_YOU_LOSING_GAMES:
            if game[0] == opponent_move:
                return game[1]
    elif outcome == 6:
        for game in OPP_TO_YOU_WINNING_GAMES:
            if game[0] == opponent_move:
                return game[1]
                
    
def your_total_score_strategy_2(file_name):
    your_score = 0
    
    rounds = convert_data_to_list(file_name)
    for round in rounds:
        opponent_move = OPPONENT_GUIDE[round[0]][1]
        outcome = OUTCOMES_GUIDE[round[2]][1]

        your_score += outcome

        if outcome == 3:
            your_score += opponent_move
        else:
            your_score += your_move(outcome, opponent_move)

    return your_score