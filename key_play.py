import sys
import pygame as pg
from scipy.interpolate import interp1d
import keyboard as k


def main():
    clock = pg.time.Clock()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        keys = pg.key.get_pressed()
        message = "0,0,0,0"
        if keys[pg.K_a]:  #to move left
            message = "1,2,255,255"
        elif keys[pg.K_d]: #to move right
            message = "2,1,255,255"
        elif keys[pg.K_w]:  #to move up
            message = "1,1,255,255"

        elif keys[pg.K_s]: #to move down
            message = "2,2,255,255"
        k.client_program(message)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
