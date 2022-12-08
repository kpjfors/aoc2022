class System:
    class File:
        def __init__(self, parent = None, name = "", size = 0):
            self.name = name
            self.size = size
            self.parent = parent

    class Directory:
        def __init__(self, parent = None, name = "", contents = []):
            self.name = name
            self.contents = contents
            self.parent = parent

    def __init__(self):
        self.root = self.Directory(name="/", contents = [])
        self.cwd = self.root

    def cd(self, dir):
        if dir == "..":
            self.cwd = self.cwd.parent
        else:
            for object in self.cwd.contents:
                if object.name == dir:
                    self.cwd = object

def interpret_line(system, line):
    if line[:4] == "$ cd":
        system.cd(line[4:].strip())
    elif line[:4] == "$ ls":
        pass #not needed for this exercise
    else:
        size, name = line.strip().split()
        if size == "dir":
            system.cwd.contents.append(system.Directory(parent = system.cwd, name = name, contents = []))
        else:
            system.cwd.contents.append(system.File(parent = system.cwd, name = name, size = int(size)))


def main(inp):
    filesystem_size = 70000000
    needed_free = 30000000

    system = System()
    for line in inp: #populate
        interpret_line(system, line)
    
    directory_sizes = []
    #find size of directories recursively:
    def ret_size(dir = system.root):
        size = 0
        for object in dir.contents:
            if isinstance(object, system.Directory):
                size += ret_size(object)
            else:
                size += object.size
        directory_sizes.append((dir.name,size))
        return size
    ret_size()

    directory_sizes = sorted(directory_sizes, key=lambda x: x[1], reverse = True)
    occupied_space = directory_sizes[0][1] #root will be first after sorting
    current_free = filesystem_size-occupied_space
    min_size = needed_free - current_free

    for name,size in directory_sizes[::-1]:
        if size >= min_size:
            return size
   

if __name__ == "__main__":
    f = open("7/input.txt", "r")
    inp = f.readlines()
    print(main(inp))