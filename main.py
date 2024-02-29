import pygame
import grid
import menu
import file

pygame.init()

birth = []
survival = []

WIDTH = 1000
HEIGHT = 1000
FPS = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

menu_window = menu.Menu(BLACK, WHITE)
menu_window.buttons_fill()

pygame.display.set_caption('Game of Life')
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

gr = grid.Grid(100, 60)
gr.fill_probability()
gr.fill_cells()

f = file.File('generations.txt')
f.clear_file()

wait = 0
run = True
mode = 'menu'

font_style = pygame.font.SysFont('arial', 20)
generations = 0
cyclicality = 0

while run:
    if mode == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if menu_window.buttons[0].collidepoint(x, y):
                    birth = [3]
                    survival = [2, 3]
                    mode = 'game'
                elif menu_window.buttons[1].collidepoint(x, y):
                    birth = [3, 6, 7, 8]
                    survival = [3, 4, 6, 7, 8]
                    mode = 'game'
        menu_window.screen_draw(window)
        menu_window.buttons_draw(window)
    elif mode == 'game':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for row in gr.cells:
            for c in row:
                c.draw(window)

        if wait == 0:
            wait = FPS / 5
            gr.check(birth, survival)
            generations += 1
            f.write_file(gr.cells)
            data = f.read_file()
            is_end = gr.control_end(data)
            if is_end[0]:
                mode = 'end'
        else:
            wait -= 1
        gen_text = font_style.render('Generations: ' + str(generations), True, RED)
        window.blit(gen_text, (0, 0))
    elif mode == 'end':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        cycle_text = font_style.render('Cyclicality: ' + str(is_end[1]), True, RED)
        window.blit(cycle_text, (200, 0))
    pygame.display.update()
    clock.tick(FPS)
    
