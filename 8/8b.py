def main(inp):
    grid = [[int(x) for x in line.strip()] for line in inp]
    grid_t = [[x[i] for x in grid] for i in range(len(grid))]
    tot_vis = 0

    def vis_trees(trees, height):
        visible = []
        for tree in trees:
            if tree < height:
                visible.append(tree)
            else:
                visible.append(tree)
                return len(visible)
        return(len(trees))

    max_vis = 0

    for i in range(len(grid)):  # vertical
        for j in range(len(grid[0])):  # horizontal
            # horizontal vis
            left_vis = vis_trees(trees=grid[i][:j][::-1], height=grid[i][j])
            right_vis = vis_trees(trees=grid[i][j+1:], height=grid[i][j])

            # vertical axis
            up_vis = vis_trees(trees=grid_t[j][:i][::-1], height=grid[i][j])
            down_vis = vis_trees(trees=grid_t[j][i+1:], height=grid[i][j])

            tot_vis = left_vis*right_vis*up_vis*down_vis
            if tot_vis > max_vis:
                max_vis = tot_vis
    return max_vis


if __name__ == "__main__":
    f = open("8/input.txt", "r")
    inp = f.readlines()
    print(main(inp))
