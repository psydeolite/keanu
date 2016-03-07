from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 0, 0 ]


display(screen)

squares=[]
#c=20
#while 
for r in range(20):
    i=r
    m=[]
    add_edge(m,c+i,c+i,0,c+1+i,c+i,0)
    add_edge(m,c+1+i,c+i,0,c+1+i,c+1+i,0)
    add_edge(m,c+1+i,c+1+i,0,c+i,c+1+i,0)
    add_edge(m,c+i,c+1+i,0,c+i,c+i,0)
    for j in range(len(m)):
        m[j]=scale2(m[j],1.0+r)
        #m[j]=rotz(m[j],30)
    squares.append(m)
    #c+=10
    #draw_lines(m,screen,color)

#for i in range(10):
#    color[1]+=50
#    color[2]+=0
for s in range(len(squares)):
    color[1]+=50
    color[2]+=0
    for k in range(len(squares[s])):
        squares[s][k]=rotz(squares[s][k],s*5)
        print 'hi'
        #translate(squares[s][k], i*10,0,0)
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
