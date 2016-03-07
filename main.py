from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]


display(screen)

squares=[]
for r in range(20):
    i=r
    m=[]
    add_edge(m,20+i,20+i,0,21+i,20+i,0)
    add_edge(m,21+i,20+i,0,21+i,21+i,0)
    add_edge(m,21+i,21+i,0,20+i,21+i,0)
    add_edge(m,20+i,21+i,0,20+i,20+i,0)
    for j in range(len(m)):
        m[j]=scale2(m[j],1.0+r)
        #m[j]=rotz(m[j],30)
    squares.append(m)
    #draw_lines(m,screen,color)

for s in range(len(squares)):
    for k in range(len(squares[s])):
        squares[s][k]=rotz(squares[s][k],s*5)
        print 'hi'
    draw_lines(squares[s],screen,color)
    
display(screen)


'''m=[]
add_edge(m,200,200,0,300,200,0)
add_edge(m,300,200,0,300,300,0)
add_edge(m,300,300,0,200,300,0)
add_edge(m,200,300,0,200,200,0)
#add_edge(m, 600,400,0,600,600,0)
#add_edge(m,0,600,600,400,600,0)
for i in range(len(m)):
    #m[i]=translate(m[i],100,0,0)
    #m[i]=rotx(m[i],30)
    #m[i]=translate(m[i],100,0,0)
    m[i]=scale2(m[i],1.5)
    m[i]=translate(m[i], -100,-50,0)
    print 'hi'

'''


#draw_lines(m, screen, color)
#display(screen)
