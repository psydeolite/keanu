from math import radians, cos, sin

def make_translate( x, y, z ):
    mat=new_matrix()
    mat[0][0]=1
    mat[0][3]=x
    mat[1][1]=1
    mat[1][3]=y
    mat[2][2]=1
    mat[2][3]=z
    mat[3][3]=1
    print'translate'
    print_matrix(mat)
    return mat
    #pass

def make_scale( x, y, z ):
    mat=new_matrix()
    mat[0][0]=x
    mat[1][1]=y
    mat[2][2]=z
    mat[3][3]=1
    return mat
    #pass
    
def make_rotX( theta ):
    mat=new_matrix()
    t=radians(theta)
    mat[0][0]=1
    mat[1][1]=cos(t)
    mat[1][2]=-1*sin(t)
    mat[2][1]=sin(t)
    mat[2][2]=cos(t)
    mat[3][3]=1
    return mat
    #pass

def make_rotY( theta ):
    mat=new_matrix()
    t=radians(theta)
    mat[0][0]=cos(t)
    mat[0][2]=-1*sin(t)
    mat[1][1]=1
    mat[2][0]=sin(t)
    mat[2][2]=cos(t)
    mat[3][3]=1
    return mat
    #pass

def make_rotZ( theta ):
    mat=new_matrix()
    t=radians(theta)
    mat[0][0]=cos(t)
    mat[0][1]=-1*sin(t)
    mat[1][0]=sin(t)
    mat[1][1]=cos(t)
    mat[2][2]=1
    mat[3][3]=1
    t=radians(theta)
    return mat
    #pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    for row in matrix:
        print row
    #pass
#n=make_scale('a','b','c');
#print_matrix(n);


def ident( matrix ):
    mat=new_matrix()
    mat[0][0]=1
    mat[1][1]=1
    mat[2][2]=1
    mat[3][3]=1
    return mat
    #pass

def scalar_mult( matrix, x ):
    for i in range(len(matrix)):
        #print 'matrix[i]: '
        #print matrix[i]
        for j in range(len(matrix[i])):
            #print 'n'
            #print matrix[i][j]
            matrix[i][j]=x*matrix[i][j]
            #n=matrix[i][j]
            #print n
            #matrix[i][j]=x*n
    return matrix
    #pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    print 'm1 rows: '+str(len(m1))
    print 'm2 cols: '+str(len(m2[0]))
    mat=new_matrix(len(m2[0]),len(m1))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                #print 'i='+str(i)
                #print 'j='+str(j)
                #print 'k='+str(k)
                mat[i][j]+=m1[i][k]*m2[k][j]
                #print str(m1[i][j])+' * '+str(m2[k][j])+' => '+str(mat[i][j])
    return mat

a=new_matrix(4,3)
b=new_matrix(2,4)

a=new_matrix(4,4)
b=new_matrix(4,4)
#print_matrix(a)
#print_matrix(b)

a[0][0]=1
a[0][1]=2
a[0][2]=3
a[0][3]=4

a[1][0]=5
a[1][1]=6
a[1][2]=7
a[1][3]=8

a[2][0]=9
a[2][1]=10
a[2][2]=11
a[2][3]=12

a[3][0]=13
a[3][1]=14
a[3][2]=15
a[3][3]=16

#b[0][0]=7
#b[1][0]=8
#b[2][0]=9
#b[3][0]=10

#b[2][0]=11
#b[2][1]=12

print 'matrix 1:'
#print_matrix(a)
scalar_mult(a, 0)

#print 'matrix 2:'
#print_matrix(a)
'''
#matrix_mult(a,b)
#print_matrix(matrix_mult(a,b))
'''
totrans=[[10],[10],[10],[10]]
t=make_translate(2,2,2)
print_matrix(matrix_mult(t,totrans))
