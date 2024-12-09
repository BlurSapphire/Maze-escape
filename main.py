from settings import *
import pygame
import sys

pygame.init()


player_pos = [3, 3]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Game')


# Function to draw the maze
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = WHITE
            if maze[row][col] == '#':
                color = BLACK
            elif maze[row][col] == 'E':
                color = GREEN
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))


def draw_player():
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE))


def move_player(direction):
    global player_pos
    x, y = player_pos

    if direction == 'W' and x > 0 and maze[x - 1][y] != '#':
        player_pos = [x - 1, y]
    elif direction == 'S' and x < len(maze) - 1 and maze[x + 1][y] != '#':
        player_pos = [x + 1, y]
    elif direction == 'A' and y > 0 and maze[x][y - 1] != '#':
        player_pos = [x, y - 1]
    elif direction == 'D' and y < len(maze[0]) - 1 and maze[x][y + 1] != '#':
        player_pos = [x, y + 1]


def game_loop():
    global player_pos

    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            move_player('W')
        if keys[pygame.K_s]:
            move_player('S')
        if keys[pygame.K_a]:
            move_player('A')
        if keys[pygame.K_d]:
            move_player('D')

        draw_maze()
        draw_player()

        if maze[player_pos[0]][player_pos[1]] == 'E':
            print("You reached the exit! Well done!")
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(15)


game_loop()
