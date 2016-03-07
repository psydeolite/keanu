from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 0, 0 ]

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
    squares.append(m)


for s in range(len(squares)):
    color[1]+=50
    color[2]+=0
    for k in range(len(squares[s])):
        squares[s][k]=rotz(squares[s][k],s*5)
        draw_lines(squares[s],screen,color)

display(screen)

