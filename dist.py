# [( 300 , 240 ) , ( 350 , 231 )]
import math as m
def shortpath(lis):
    distances={}
    t1=lis[0]
    for i in range(1,len(lis)):
        t2 = lis[i]
        dist = m.sqrt((t1[0] - t2[0])**2 + (t2[1] - t1[1])**2)
        #distances.update({i:dist})
        distances[i]=dist
    return distances

'''
            90
            |      left
            |
            |
180 - - - - - - - - - - 0                original axis
            |
            | 
            |      right
            270

'''
def directions(o1,o2): #(45,1) -> 45 degreees to the right (90,2) -> 90 degrees to the left, o2 is always from our axis
    o1_d = o1[1]
    o2_d = o2[1]
    o1_a = o1[0]
    o2_a = o2[0]
    if o1_d == o2_d:
        atm = abs(o1_a - o2_a)
    elif o1_d != o2_d:
        atm = o1_a + o2_a
    return (atm,o2_d)

if __name__ == '__main__':
    #x = shortpath([( 300 , 240 ) , ( 350 , 231 ), (300,110) , (400,120)])
    #print(x)
    atm = directions((45,2),(90,1))
    print(directions((45,2),(90,1)))
    if atm[0] > 90:
        if atm[1] == 1:
            ins = 'move bot right and ' + str(atm[0]-90)+'º diagonally'
        else:
            ins = 'move bot left and ' + str(atm[0]-90)+'º diagonally'
    if atm[0] < 90:
        if atm[1] == 1:
            ins = 'move bot ' + str(atm[0])+'º diagonally'
        else:
            ins = 'move bot ' + str(atm[0])+'º diagonally'
    if atm[0] == 180:
        ins = 'MOVE BOT BACK!'
    print(ins)

        
        
