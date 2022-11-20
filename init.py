import pygame
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

COLUMNS = 50
ROWS = 50

BOX_WIDTH = WINDOW_WIDTH // COLUMNS
BOX_HEIGHT = WINDOW_HEIGHT // ROWS

BLACK = (0, 0, 0)
SLATE = (50, 50, 50)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
CYAN = (0, 200, 200)
GREY = (90, 90, 90)
YELLOW = (200, 200, 0)

grid = []
queue = []
path = []

def create_grid(Box):
    for i in range(COLUMNS):
        arr = []
        for j in range(ROWS):
            arr.append(Box(i, j))
        grid.append(arr)
  

def set_neighbours():
  for i in range(COLUMNS):
      for j in range(ROWS):
          grid[i][j].set_neighbours()


def color():
    for i in range(COLUMNS):
        for j in range(ROWS):
            box = grid[i][j]
            box.draw(WINDOW, SLATE)

            if box.queued:
                box.draw(WINDOW, RED)
            if box.visited:
                box.draw(WINDOW, GREEN)
            if box in path:
                box.draw(WINDOW, BLUE)

            if box.start:
                box.draw(WINDOW, CYAN)
            if box.wall:
                box.draw(WINDOW, GREY)
            if box.target:
                box.draw(WINDOW, YELLOW)
