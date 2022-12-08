def main(inp):
    inp_size_stack = 4
    num_stacks = int(len(inp[0])/inp_size_stack)
    stacks = [[] for x in range(num_stacks)]
    stacks_built = False
    for line in inp:
        # only true for buid instructions
        if len(line) > 1 and line.strip()[0] == "[":
            for stack in range(num_stacks):
                crate = line[int(stack*inp_size_stack)
                                 :int((stack+1)*inp_size_stack)]
                if crate.strip() == "":
                    pass
                else:
                    stacks[stack].append(crate[1:-2])
        elif stacks_built == False:
            for stack in stacks:
                stack.reverse()
            stacks_built = True
        if line[0] == "m":  # only true for move instructions
            unparsed = line.strip().split(" ")
            cnt, fr, to = [int(x) for x in unparsed[1::2]]
            for i in stacks[fr-1][-cnt:][::-1]:
                stacks[to-1].append(i)
            stacks[fr-1] = stacks[fr-1][:-cnt]
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    f = open("5/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
