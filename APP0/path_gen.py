map =   [[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
		 [1, 0, 1, 1, 4, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		 [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
		 [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
		 [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
		 [2, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 3],
		 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
		 [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
		 [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		 [1, 4, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
		 [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]]

"""
dzded
"""

map13 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 4, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1], [1, 4, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 4, 1], [1, 1, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 1, 3], [1, 4, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 4, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1], [1, 4, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 4, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 1]]

map14 = [[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 3], [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1]]

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 2:
            start = [x, y]
        if map[y][x] == 3:
            end = [x, y]

class Node():
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.calculate_cost()
    
    def __eq__(self, other):
        if (isinstance(other, Node)):
            return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"x:{self.x}-y:{self.y}, parent:{self.parent}"
    
    def __repr__(self):
        return f"x:{self.x}, y:{self.y}, cost:{self.cost}"

    def calculate_cost(self):
        self.cost = abs(self.x-end[0]) + abs(self.y-end[1])
        if self.parent != None:
            self.cost += self.parent.cost - abs(self.parent.x-end[0]) - abs(self.parent.y-end[1])

startNode = Node(start[0], start[1], None)
endNode = Node(end[0], end[1], None)

visited = [startNode]
frontier = []
currentNode = startNode

while True:
    borderNodes = [Node(currentNode.x-1, currentNode.y, currentNode), Node(currentNode.x+1, currentNode.y, currentNode),
                   Node(currentNode.x, currentNode.y-1, currentNode), Node(currentNode.x, currentNode.y+1, currentNode)]

    for node in borderNodes:
        if node == endNode:
            frontier.append(node)
    
    if endNode in frontier:
        break

    for node in borderNodes:
        if node.x < 0 or node.x > 15 or node.y < 0 or node.y > 11:
            continue
        elif map[node.y][node.x] == 1 or map[node.y][node.x] == 3:
            if node not in visited and node not in frontier:
                frontier.append(node)

    bestCost = 999999
    bestNode = None
    for node in frontier:
        if node.cost < bestCost:
            bestCost = node.cost
            bestNode = node

    currentNode = bestNode
    frontier.remove(currentNode)
    visited.append(currentNode)

for node in frontier:
    if node == endNode:
        final = node

print("done")

path = str(final)
temp_arr = path.split(", ")
path_arr = []
for a in temp_arr:
    if a == 'parent:None':
        continue
    path_arr.append(a.replace("parent:", ""))
path_arr.reverse()

with open("solver.py", "w") as f:
    pass

with open("solver.py", "a") as f:
    pos = path_arr[0]
    x, y = int(pos[pos.index("x:")+2:pos.index("-")]), int(pos[pos.index("y:")+2:])
    path_arr.pop(0)
    facing = None
    while len(path_arr) != 0:
        pos = path_arr[0]
        next_x, next_y = int(pos[pos.index("x:")+2:pos.index("-")]), int(pos[pos.index("y:")+2:])
        path_arr.pop(0)
        if facing == None:
            if next_x == x+1:
                f.write("while get_direction() != EAST:\n\tturn_left()\n")
                facing = "EAST"
            elif next_x == x-1:
                f.write("while get_direction() != WEST:\n\tturn_left()\n")
                facing = "WEST"
            elif next_y == y+1:
                f.write("while get_direction() != SOUTH:\n\tturn_left()\n")
                facing = "SOUTH"
            elif next_y == y-1:
                f.write("while get_direction() != NORTH:\n\tturn_left()\n")
                facing = "NORTH"
        
        print([x, y], [next_x, next_y], facing)
        if (next_x == x+1 and facing=="EAST") or (next_x == x-1 and facing=="WEST") or (next_y == y+1 and facing=="SOUTH") or (next_y == y-1 and facing=="NORTH"):
            f.write(f"move() # going to [{next_x}, {next_y}]\n")
        else:
            if (next_x == x+1 and facing=="SOUTH") or (next_x == x-1 and facing=="NORTH") or (next_y == y-1 and facing=="EAST") or (next_y == y+1 and facing=="WEST"):
                f.write("turn_left()\n")
                if facing == "SOUTH":
                    facing = "EAST"
                elif facing == "EAST":
                    facing = "NORTH"
                elif facing == "NORTH":
                    facing = "WEST"
                elif facing == "WEST":
                    facing = "SOUTH"
            elif (next_x == x+1 and facing=="NORTH") or (next_x == x-1 and facing=="SOUTH") or (next_y == y-1 and facing=="WEST") or (next_y == y+1 and facing=="EAST"):
                f.write("turn_right()\n")
                if facing == "SOUTH":
                    facing = "WEST"
                elif facing == "WEST":
                    facing = "NORTH"
                elif facing == "NORTH":
                    facing = "EAST"
                elif facing == "EAST":
                    facing = "SOUTH"
            f.write(f"move() # going to [{next_x}, {next_y}]\n")

        x, y = next_x, next_y