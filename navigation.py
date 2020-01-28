import sys
import pygame as pg
from scipy.interpolate import interp1d


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    rect = pg.Rect(300, 220, 20, 20)
    velocity = (0, 0)
    done = False
    pg.joystick.init()
    joystick = pg.joystick.Joystick(0)
    print(joystick)
    joystick.init()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        axis1 = joystick.get_axis( 1 ) #for forward movement
        axis0 = joystick.get_axis( 0 ) #for left and right movement
        axis3 = joystick.get_axis( 4 ) #for speed control
        button = joystick.get_button( 0 )
        print(axis3)
        axis3*=-1 #to reverse the mapping
        axis3+=1 #now range = (0,2)
        if axis3 < 0.005:
            axis3=0
        m = interp1d([0,2],[0,12]) #linear mapping funtion
        speed = int(m(axis3)) #stm can handle only integer
        print("speed",speed)
        hat = joystick.get_hat( 0 )
        keys = pg.key.get_pressed()
        if keys[pg.K_a] or axis0 <= -0.85 and hat == (0,0):  #to move left
            if button == 0:    
                rect.x -= speed
            if button ==1:
                rect.x -= 5
        elif keys[pg.K_d] or axis0 >= 0.85 and hat == (0,0): #to move right
            if button == 0:
                rect.x += speed
            if button ==1:
                rect.x += 5
        elif keys[pg.K_w] or axis1 <= -0.85 and hat == (0,0):  #to move up
            if button == 0:
                rect.y -= speed
            if button ==1:
                rect.y -= 5
        elif keys[pg.K_s] or axis1 >= 0.85 and hat == (0,0): #to move down
            if button == 0:
                rect.y += speed
            if button ==1:
                rect.y += 5


        if hat == (-1,0):  #to move left
            rect.x -= 3
        if hat == (1,0): #to move right
            rect.x += 3
        if hat == (0,1):  #to move up
            rect.y -= 3
        if hat == (0,-1): #to move down
            rect.y += 3


        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()