def main(inp):
    top_three_cal = [0, 0, 0]
    curr_cal = 0
    for i in inp:
        if i.isspace():
            if curr_cal > min(top_three_cal):
                top_three_cal[top_three_cal.index(
                    min(top_three_cal))] = curr_cal
            curr_cal = 0
        else:
            curr_cal += int(i)
    return sum(top_three_cal)


if __name__ == "__main__":
    f = open("1/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
