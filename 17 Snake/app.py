import pygame
import random
import tkinter as tk
from tkinter import messagebox


# --------- Cube Class ----------
class Cube:
    rows = 20
    width = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.width // self.rows
        i, j = self.pos
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        if eyes:
            centre = dis // 2
            radius = 3
            circle1 = (i * dis + centre - radius, j * dis + 8)
            circle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle1, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle2, radius)


# --------- Snake Class ----------
class Snake:
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body = [self.head]
        self.dirnx = 0
        self.dirny = 1
        self.turns = {}

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirnx, self.dirny = -1, 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_RIGHT]:
                self.dirnx, self.dirny = 1, 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_UP]:
                self.dirnx, self.dirny = 0, -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_DOWN]:
                self.dirnx, self.dirny = 0, 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, cube in enumerate(self.body):
            pos = cube.pos[:]
            if pos in self.turns:
                turn = self.turns[pos]
                cube.move(*turn)
                if i == len(self.body) - 1:
                    self.turns.pop(pos)
            else:
                if cube.dirnx == -1 and cube.pos[0] <= 0:
                    cube.pos = (cube.rows - 1, cube.pos[1])
                elif cube.dirnx == 1 and cube.pos[0] >= cube.rows - 1:
                    cube.pos = (0, cube.pos[1])
                elif cube.dirny == 1 and cube.pos[1] >= cube.rows - 1:
                    cube.pos = (cube.pos[0], 0)
                elif cube.dirny == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], cube.rows - 1)
                else:
                    cube.move(cube.dirnx, cube.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = [self.head]
        self.dirnx, self.dirny = 0, 1
        self.turns = {}

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1:
            new_pos = (tail.pos[0] - 1, tail.pos[1])
        elif dx == -1:
            new_pos = (tail.pos[0] + 1, tail.pos[1])
        elif dy == 1:
            new_pos = (tail.pos[0], tail.pos[1] - 1)
        else:
            new_pos = (tail.pos[0], tail.pos[1] + 1)

        new_cube = Cube(new_pos)
        new_cube.dirnx = dx
        new_cube.dirny = dy
        self.body.append(new_cube)

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            cube.draw(surface, eyes=(i == 0))


# --------- Utility Functions ----------
def draw_grid(width, rows, surface):
    gap = width // rows
    for l in range(rows):
        pygame.draw.line(surface, (255, 255, 255), (l * gap, 0), (l * gap, width))
        pygame.draw.line(surface, (255, 255, 255), (0, l * gap), (width, l * gap))


def redraw_window(surface, snake, snack, width, rows):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, snake):
    positions = [cube.pos for cube in snake.body]

    while True:
        x, y = random.randrange(rows), random.randrange(rows)
        if (x, y) not in positions:
            break
    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


# --------- Main Game Loop ----------
def main():
    width, rows = 500, 20
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Snake Game")

    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, snake), color=(0, 255, 0))

    clock = pygame.time.Clock()
    run = True

    while run:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()

        if snake.body[0].pos == snack.pos:
            snake.add_cube()
            snack = Cube(random_snack(rows, snake), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in [cube.pos for cube in snake.body[x + 1:]]:
                print("Score:", len(snake.body))
                message_box("You Lost!", "Play again...")
                snake.reset((10, 10))
                break

        redraw_window(win, snake, snack, width, rows)

    pygame.quit()


if __name__ == "__main__":
    main()
