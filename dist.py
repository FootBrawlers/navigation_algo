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
if __name__ == '__main__':
    x = shortpath([( 300 , 240 ) , ( 350 , 231 ), (300,110) , (400,120)])
    print(x)
        
        
