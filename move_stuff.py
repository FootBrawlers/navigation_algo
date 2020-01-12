import sys
import pygame as pg
import dist as di
import random as r


def main():
    screen = pg.display.set_mode((640, 497))
    clock = pg.time.Clock()
    rect1 = pg.Rect(300, 220, 20, 20)
    rect2 = pg.Rect(300, 220, 20, 20)
    obs = pg.Rect(350, 190, 30, 50)
    velocity = (10, 10)
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
        pg.draw.rect(screen, (40, 40, 40), obs)
        pg.draw.rect(screen, (150, 200, 20), rect1)
        pg.draw.rect(screen, (200, 100, 20), rect2)
        #pg.draw.circle(screen, (200, 150, 20), (300,220),5)
        
        lis = [(rect1.left,rect1.bottom),(rect2.left,rect2.bottom)]

        distance_i = di.shortpath(lis)
        distances=[]
        
        for i in distance_i:
            distances.append(distance_i[i])

            

        s_p = str(min(distances))[0:5]
        text3 = font.render(s_p,True,(0,255,0))
        textRect3 = text3.get_rect()
        textRect3.center = (300,40)
            


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
        screen.blit(text3,textRect3)
        p_f=1#passing flag

        if min(distances) <= 220 and (rect1.bottom < (obs.bottom-obs.width) and rect2.bottom < (obs.bottom-obs.width) or ( rect1.left < obs.left and rect2.left < obs.left ) or (rect1.bottom > (obs.bottom) and rect2.bottom > (obs.bottom)or (rect1.left>obs.left+obs.width and rect2.left>obs.left+obs.width))):
            if keys[pg.K_p]:
                p_f*=-1
                #pg.draw.circle(screen, (200, 150, 20), (rect2.left,rect2.bottom),5)
            #pg.draw.circle(screen, (200, 150, 20), (rect1.left,rect1.bottom),5)
        
        if p_f == -1:
            pg.draw.circle(screen, (200, 150, 20), (rect2.left,rect2.bottom),5)
        else:
            pg.draw.circle(screen, (200, 150, 20), (rect1.left,rect1.bottom),5)

        
        if keys[pg.K_c]:
            if rect1.bottom < (obs.bottom) and rect1.bottom > (obs.bottom-obs.height):
            #if 1==1:
                print('hey')
                md = 1
                '''
                while(rect1.bottom < obs.bottom+30):
                    ###time.sleep(100)
                    rect1.y +=2
                    clock.tick(1200)
                    pg.draw.rect(screen, (150, 200, 20), rect1)
                if rect1.left > rect2.left:
                    while(rect1.left > rect2.left+30):
                        rect1.x-=2
                        clock.tick(1200)
                        pg.draw.rect(screen, (150, 200, 20), rect1)
                elif rect1.left < rect2.left:
                    while(rect1.left < rect2.left-30):
                        rect1.x+=2
                        clock.tick(1200)
                        pg.draw.rect(screen, (150, 200, 20), rect1)
                        '''
            


            if md==1:
                rect1.y+=10
                if rect1.bottom > obs.bottom+30 :
                    print('came here')
                    md = 0
                    ml = 1
            if md == 0 and ml ==1:
                if rect1.left > rect2.left+100:
                    rect1.x-=10
                if float(s_p) < 145:
                    x = r.randint(0,4)
                    if x == 0:
                        rect2.x-=10
                    if x == 1:
                        rect2.x += 10
                    if x == 2:
                        rect2.y += 10
                    if x == 3:
                        rect2.y -= 10

                elif rect1.left < rect2.left-100:
                    rect1.x+=10

        if keys[pg.K_f]:
                print('f mode')
                if rect1.left > 150:
                    rect1.x-=10
                if rect1.bottom < 140:
                    rect1.y+=10
                if rect1.y > 300:
                    rect1.y-=10
                if rect1.left <160 and rect1.bottom >=140 and rect1.bottom <=320:
                    pg.draw.circle(screen, (200, 150, 20), (10,240),5)
        if keys[pg.K_m]:
            if float(s_p) > 50:
                if rect2.bottom > rect1.bottom:
                    rect2.y-=20
                if rect2.bottom < rect1.bottom:
                    rect2.y+=20
                #if rect2.left > rect1.left:
                    #rect2.x-=18
                if rect2.left > rect1.left:
                    rect2.x-=20
            if rect2.left < rect1.left:
                    rect2.x+=20


        pg.display.flip()
        clock.tick(1200)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
