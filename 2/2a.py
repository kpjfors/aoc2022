def main(inp):
    score_selection = {
        "A": 1, #Rock
        "B": 2, #Paper
        "C": 3, #Scissor
        "X": 1, #Rock
        "Y": 2, #Paper
        "Z": 3, #Scissor
    }

    score_result = {
        "loss": 0,
        "draw": 3,
        "win": 6
    }

    result_dict={
        2:"loss",
        1:"win",
        0:"draw",
        -1:"loss", 
        -2:"win"
    }

    tot_score = 0
    cache = {}

    for row in inp:
        row = row.strip()
        if row in cache:
            tot_score += cache[row]
        else:
            opponent_selection, our_selection = [x.strip() for x in row.split(" ")]
            game_score = score_selection[our_selection] + score_result[result_dict[score_selection[our_selection]-score_selection[opponent_selection]]]
            cache[row] = game_score
            tot_score += game_score
    return tot_score

if __name__ == "__main__":
    f = open("2/input.txt", "r")
    nums = f.readlines()
    print(main(nums))