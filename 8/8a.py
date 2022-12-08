def main(inp):
    grid = [[int(x) for x in line.strip()] for line in inp]
    grid_t = [[x[i] for x in grid] for i in range(len(grid))]
    tot_vis = 0

    for i in range(len(grid)):  # vertical
        for j in range(len(grid[0])):  # horizontal
            # horizontal vis
            left_vis = [x for x in grid[i][:j] if x > grid[i][j]]
            right_vis = [x for x in grid[i][j+1:] if x]
            horizontal_vis = (grid[i][j] > max(
                grid[i][:j], default=-1)) or (grid[i][j] > max(grid[i][j+1:], default=-1))

            # vertical vis
            vertical_vis = (grid[i][j] > max(
                grid_t[j][i+1:], default=-1)) or (grid[i][j] > max(grid_t[j][:i], default=-1))

            if horizontal_vis or vertical_vis:
                tot_vis += 1
    return tot_vis


if __name__ == "__main__":
    f = open("8/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
