def main(inp):
    max_cal = 0
    curr_cal = 0
    for i in inp:
        if i.isspace():
            curr_cal = 0
        else:
            curr_cal += int(i)
        if curr_cal > max_cal:
            max_cal = curr_cal
    return max_cal


if __name__ == "__main__":
    f = open("1/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
