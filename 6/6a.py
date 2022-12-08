def main(inp):
    seq = inp[0]
    i = 0
    while 1:
        substr = seq[i:i+4]
        if len(set(substr)) == len(substr):
            return i+4
        i += 1


if __name__ == "__main__":
    f = open("6/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
