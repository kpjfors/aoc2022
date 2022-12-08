def main(inp):
    score = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = {i[1]: i[0] for i in enumerate([x for x in score])}
    tot_sum = 0
    for i in inp:
        firsthalf = i[:int(len(i)/2)]
        secondhalf = i[int(len(i)/2):]
        firstcount = set(firsthalf)
        secondcount = set(secondhalf.strip())
        sum_score = score[firstcount.intersection(secondcount).pop()] + 1
        tot_sum += sum_score
    return(tot_sum)


if __name__ == "__main__":
    f = open("3/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
