def main(inp):
    overlapping = 0
    for i in inp:
        first, second = i.strip().split(",")
        first = [int(x) for x in first.split("-")]
        second = [int(x) for x in second.split("-")]
        if first[0] < second[0] and first[1] < second[0]:
            pass
        elif first[0] > second[1] and first[1] > second[1]:
            pass
        else:
            overlapping += 1
    return overlapping


if __name__ == "__main__":
    f = open("4/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
