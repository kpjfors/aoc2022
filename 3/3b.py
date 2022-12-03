def main(inp):
    score = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = {i[1]:i[0] for i in enumerate([x for x in score])}
    tot_sum = 0
    candidates = set()
    for i in inp:
        rucksack = set(i.strip())
        if len(candidates) == 0:
            candidates = set(rucksack)
        else:
            candidates = candidates.intersection(set(i))
        if len(candidates) == 1:
            tot_sum += score[candidates.pop()] + 1
    return(tot_sum)

if __name__ == "__main__":
    f = open("3/input.txt", "r")
    inp = f.readlines()
    print(main(inp))