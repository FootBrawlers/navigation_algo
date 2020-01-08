import sys
import pygame as pg


def main():
    screen = pg.display.set_mode((640, 497))
    clock = pg.time.Clock()
    rect1 = pg.Rect(300, 220, 20, 20)
    rect2 = pg.Rect(300, 220, 20, 20)
    velocity = (0, 0)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        font = pg.font.Font('freesansbold.ttf', 16)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:  #to move left
            rect1.x -= 10
        if keys[pg.K_d]: #to move right
            rect1.x += 10
        if keys[pg.K_w]:
            rect1.y-= 10
        if keys[pg.K_s]:
            rect1.y+=10

        if keys[pg.K_j]:  #to move left
            rect2.x -= 10
        if keys[pg.K_l]: #to move right
            rect2.x += 10
        if keys[pg.K_i]:
            rect2.y-= 10
        if keys[pg.K_k]:
            rect2.y+=10

        if keys[pg.K_q]:
            print('green bot position: (',rect1.left,',',rect1.bottom,')')
            
        if keys[pg.K_e]:
            print('orange bot position: (',rect2.left,',',rect2.bottom,')')


        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect1)
        pg.draw.rect(screen, (200, 100, 20), rect2)
        #pg.draw.circle(screen, (200, 150, 20), (300,220),5)


        g_pos ='green bot position: ('+str(rect1.left)+','+str(rect1.bottom)+')'

        o_pos = 'orange bot position: ('+str(rect2.left)+','+str(rect2.bottom)+')'

        text1 = font.render(g_pos, True, (0,255,0))
        text2 = font.render(o_pos, True, (0,255,0))
        textRect1 = text1.get_rect()
        textRect2 = text2.get_rect()
        textRect1.center = (120, 40)
        textRect2.center = (510, 40)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        pg.draw.circle(screen, (200, 150, 20), (rect1.left,rect1.bottom),5)
        
        

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
