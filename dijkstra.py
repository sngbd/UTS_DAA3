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

# Create Grid
create_grid(Box) 

# Set Neighbours
set_neighbours()

start_box = grid[0][0]
start_box.start = True
start_box.visited = True
queue.append(start_box)

def dijkstra_algorithm(target_box):
    current_box = queue.pop(0)
    current_box.visited = True
    if current_box == target_box:
        while current_box.prior != start_box:
            path.append(current_box.prior)
            current_box = current_box.prior
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
    target_box_set = False
    searching = True
    target_box = None

    while True:
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # Draw Wall
                if event.buttons[0]:
                    i = x // BOX_WIDTH
                    j = y // BOX_HEIGHT
                    grid[i][j].wall = True
                # Set Target
                if event.buttons[2] and not target_box_set:
                    i = x // BOX_WIDTH
                    j = y // BOX_HEIGHT
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
            # Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                if event.key == pygame.K_SPACE:
                    begin_search = True
        if begin_search:
            if len(queue) > 0 and searching:
                searching = dijkstra_algorithm(target_box)
            else:
                if searching:
                    searching = False
                    print('There is no solution.')

        WINDOW.fill(BLACK)
        
        color()
        pygame.display.flip()
  
main()
