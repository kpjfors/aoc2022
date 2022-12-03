def main(inp):
    score_selection = {
        "A": 1, #Rock
        "B": 2, #Paper
        "C": 3, #Scissor
    }

    move_decider = {
        "X": -1, #loss
        "Y": 0, #draw
        "Z": 1 #win
    }

    score_result = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    tot_score = 0
    cache = {}

    for row in inp:
        row = row.strip()
        if row in cache:
            tot_score += cache[row]
        else:
            game_score = 0
            opponent_selection, game_result = [x.strip() for x in row.split(" ")]
            our_selection = (score_selection[opponent_selection] + move_decider[game_result] ) % 3
            if our_selection == 0:
                our_selection = 3 
            game_score = our_selection + score_result[game_result]
            cache[row] = game_score
            tot_score += game_score
    return tot_score

if __name__ == "__main__":
    f = open("2/input.txt", "r")
    inp = f.readlines()
    print(main(inp))