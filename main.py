from knight_tour import KnightTour
import pygame
import sys


def draw_background():
    screen.fill(blackTileColor)
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, whiteTileColor, (tileSize * j, tileSize * i, tileSize, tileSize), 0)


def draw_tiles():
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if knight_pos == (i, j):
                pygame.draw.circle(screen, knightTileColor,
                                   (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4, 0)
            elif knight_tour.board[i][j] != 0:
                pygame.draw.circle(screen, visitedTileColor,
                                   (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4,  0)


def draw_line(start, end):
    pygame.draw.line(screen, lineColor,
                     (tileSize * start[1] + tileSize // 2, tileSize * start[0] + tileSize // 2),
                     (tileSize * end[1] + tileSize // 2, tileSize * end[0] + tileSize // 2), 10)


board_size = (20, 20)
screenSizeX = 800
screenSizeY = 800

if screenSizeX//board_size[1] >= screenSizeY//board_size[0]:
    tileSize = screenSizeY // board_size[0]
else:
    tileSize = screenSizeX // board_size[1]

knight_tour = KnightTour(board_size=board_size)
pygame.init()
screen = pygame.display.set_mode((tileSize*board_size[1], tileSize*board_size[0]))
clock = pygame.time.Clock()
fps = 5

whiteTileColor = (245, 245, 245)
blackTileColor = (100, 100, 100)
visitedTileColor = (153, 51, 51)
knightTileColor = (255, 102, 102)
lineColor = (255, 102, 102)

knight_pos = (0, 0)
draw_background()
draw_tiles()


skip = True
runUpdate = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                runUpdate = False

            if event.key == pygame.K_q:
                fps += 1
            if event.key == pygame.K_a:
                fps -= 1
                if fps == 0:
                    fps = 1
            # if event.key == pygame.K_r:
            #     board = [[emptyTile for _ in range(n)] for _ in range(n)]
            #     knightXPos = 0
            #     knightYPos = 0
            #     board[knightYPos][knightXPos] = knightTile
            #     draw_background()
            #     draw_tiles()
            #     moveNum = 0
            #     skip = True
    if runUpdate:
        last_knight_pos = knight_pos
        if last_knight_pos:
            knight_pos = knight_tour.warnsdroff(knight_pos, GUI=True)
            board = knight_tour.board
            # knight_tour.print_board()
            if knight_pos:
                draw_line(last_knight_pos, knight_pos)
            draw_tiles()
    pygame.display.set_caption("Knight\'s Tour " + str(fps) + "fps")
    pygame.display.update()
    # msElapsed = clock.tick(fps)
