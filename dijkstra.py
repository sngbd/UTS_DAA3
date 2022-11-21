from init import *

pygame.display.set_caption("Dijkstra Path Finding Algorithm")

class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None
    
    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * BOX_WIDTH, self.y * BOX_HEIGHT, BOX_WIDTH - 2, BOX_HEIGHT - 2))
    
    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < COLUMNS - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < ROWS - 1:
            self.neighbours.append(grid[self.x][self.y + 1])

create_grid(Box) 

set_neighbours()

def dijkstra_algorithm(start_box, target_box):
    current_box = queue.pop(0)
    current_box.visited = True
    if current_box == target_box:
        while current_box.prior != start_box:
            path.append(current_box.prior)
            current_box = current_box.prior
        start_grid = (start_box.x, start_box.y)
        target_grid = (target_box.x, target_box.y)
        print("Start box:", start_grid)
        print("Target box:", target_grid) 
        path_grid = []
        for p in reversed(path):
            path_grid.append((p.x, p.y))
        print("Path length:", len(path_grid))
        return False
    else:
        for neighbour in current_box.neighbours:
            if not neighbour.queued and not neighbour.wall:
                neighbour.queued = True
                neighbour.prior = current_box
                queue.append(neighbour)
    return True
    
def main():
    begin_search = False
    searching = True
    target_box = None
    start_box = None
    steps = 0
    done = False

    if (len(sys.argv) > 1 and sys.argv[1] == "--maze"):
        start_box, target_box = init_maze()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if begin_search:
                    continue

                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                i = x // BOX_WIDTH
                j = y // BOX_HEIGHT

                if event.buttons[0] and not grid[i][j].start and not grid[i][j].target:
                    grid[i][j].wall = True
                if event.buttons[2] and not start_box and not grid[i][j].target and not grid[i][j].wall:
                    start_box = grid[i][j]
                    start_box.start = True
                    start_box.visited = True
                    queue.append(start_box)
                elif event.buttons[2] and not target_box and not grid[i][j].start and not grid[i][j].wall:
                    target_box = grid[i][j]
                    target_box.target = True

            if event.type == pygame.KEYDOWN and target_box:
                if event.key == pygame.K_SPACE:
                    begin_search = True

        if begin_search:
            if len(queue) > 0 and searching:
                searching = dijkstra_algorithm(start_box, target_box)
                steps += 1
            else:
                if searching:
                    searching = False
                    print("There is no solution.")
                if not done:
                    done = True
                    print("Steps:", steps)

        WINDOW.fill(BLACK)
        
        color()
        pygame.display.flip()
  
main()
