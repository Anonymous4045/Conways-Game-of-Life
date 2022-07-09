import pygame, time

framerate = 3

pygame.init()

cell_icon = pygame.image.load('cell.png')

display = pygame.display
screen = display.set_mode((1000, 800))
display.set_caption("Conway's Game of life")
display.set_icon(cell_icon)


def show(cells):
    for c in cells:
        screen.blit(cell_icon, (c[0], c[1]))


cells = []
new_cells=[]

while True:
    placing = True
    while placing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                placing = False
                pygame.quit()
                quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cell = event.pos[0]-event.pos[0]%32, event.pos[1]-event.pos[1]%32
                    if cell not in cells: cells.append(cell)
                    else: cells.remove(cell)
            elif event.type == pygame.KEYDOWN:
                if event.key == 13 or event.key == pygame.K_SPACE: placing = False
                if event.key == pygame.K_z:
                    try:
                        cells.remove(cells[-1])
                    except IndexError:
                        cells = []
                if event.key == pygame.K_c: cells = []
                if event.key == pygame.K_w:
                    for cell in cells:
                        new_cells.append((cell[0], cell[1]+32))
                if event.key == pygame.K_a:
                    for cell in cells:
                        new_cells.append((cell[0]+32, cell[1]))
                if event.key == pygame.K_s:
                    for cell in cells:
                        new_cells.append((cell[0], cell[1]-32))
                if event.key == pygame.K_d:
                    for cell in cells:
                        new_cells.append((cell[0]-32, cell[1]))
                if new_cells:
                    cells = new_cells
                    new_cells = []

        screen.fill((0, 0, 0))
        show(cells)
        display.flip()


    def check(cell):
        global new_cells
        n,x,y=0,cell[0],cell[1]
        if (x+32,y) in cells: n+=1
        if (x,y+32) in cells: n+=1
        if (x+32,y-32) in cells: n+=1
        if (x+32,y+32) in cells: n+=1
        if (x-32,y+32) in cells: n+=1
        if (x-32,y) in cells: n+=1
        if (x-32,y-32) in cells: n+=1
        if (x,y-32) in cells: n+=1
        if n == 3 and cell not in new_cells: new_cells.append(cell)

    calc = True
    while calc:
        for cell in cells:
            neighbors, x, y = 0, cell[0], cell[1]
            if (x+32, y) in cells: neighbors += 1
            check((x+32, y))
            if (x, y+32) in cells: neighbors += 1
            check((x, y+32))
            if (x+32, y-32) in cells: neighbors += 1
            check((x+32, y-32))
            if (x+32, y+32) in cells: neighbors +=1
            check((x+32, y+32))
            if (x-32, y+32) in cells: neighbors += 1
            check((x-32, y+32))
            if (x-32, y) in cells: neighbors += 1
            check((x-32, y))
            if (x-32, y-32) in cells: neighbors += 1
            check((x-32, y-32))
            if (x, y-32) in cells: neighbors += 1
            check((x, y-32))
            if neighbors == 2 or neighbors == 3:
                if cell not in new_cells: new_cells.append(cell)

        if cells == new_cells:
            calc = False
        cells = new_cells
        new_cells = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    calc = False
                if event.key == pygame.K_w:
                    for cell in cells:
                        new_cells.append((cell[0], cell[1]+32))
                if event.key == pygame.K_a:
                    for cell in cells:
                        new_cells.append((cell[0]+32, cell[1]))
                if event.key == pygame.K_s:
                    for cell in cells:
                        new_cells.append((cell[0], cell[1]-32))
                if event.key == pygame.K_d:
                    for cell in cells:
                        new_cells.append((cell[0]-32, cell[1]))
                if new_cells:
                    cells = new_cells
                    new_cells = []

        screen.fill((0, 0, 0))
        show(cells)
        display.flip()

        time.sleep(framerate**-1)

