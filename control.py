import sys
import pygame as pg
from scipy.interpolate import interp1d
import client as cl

def main():
    clock = pg.time.Clock()
    pg.joystick.init()
    joystick = pg.joystick.Joystick(0)
    print(joystick)
    joystick.init()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        axis1 = joystick.get_axis( 1 ) #for forward movement
        axis0 = joystick.get_axis( 0 ) #for left and right movement
        axis3 = joystick.get_axis( 4 ) #for speed control
        print(axis3)
        axis3*=-1 #to reverse the mapping
        axis3+=1 #now range = (0,2)
        if axis3 < 0.005:
            axis3=0
        m = interp1d([0,2],[0,12]) #linear mapping funtion
        speed = int(m(axis3)) #stm can handle only integer
        print("speed",speed)
        cl.client_program(str(axis0)+','+str(axis1)+','+str(speed))
        clock.tick(30)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
