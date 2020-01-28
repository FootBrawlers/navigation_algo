import sys
import pygame as pg
from scipy.interpolate import interp1d
import server as se


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    rect = pg.Rect(300, 220, 20, 20)
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        list1 = se.server_program()
        list1 = list1.split(',')
        axis0 = float(list1[0])
        axis1= float(list1[1])
        speed = float(list1[2])
        button = 0
        if axis0 <= -0.85:  #to move left
            if button == 0:    
                rect.x -= speed
            if button ==1:
                rect.x -= 5
        elif axis0 >= 0.85: #to move right
            if button == 0:
                rect.x += speed
            if button ==1:
                rect.x += 5
        elif  axis1 <= -0.85:  #to move up
            if button == 0:
                rect.y -= speed
            if button ==1:
                rect.y -= 5
        elif  axis1 >= 0.85: #to move down
            if button == 0:
                rect.y += speed
            if button ==1:
                rect.y += 5


        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()