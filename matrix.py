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
    t=radians(t)
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
    t=radians(t)
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
n=make_scale('a','b','c');
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
        for j in range(len(matrix[i])):
            matrix[i][j]=x*matrix[i][j]
    return matrix
    #pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #print w
    #l=len(m2)
    #print l
    print 'm1 rows: '+str(len(m1))
    print 'm2 cols: '+str(len(m2[0]))
    mat=new_matrix(len(m2[0]),len(m1))
    #print_matrix(m1)
    ##print ''
    #print_matrix(m2)
    print ''
    #print_matrix(mat)
    #i=m1 row index
    for i in range(len(m1)):
        #j=m2 col index
        for j in range(len(m2[0])):
            #k=m2 row index
            for k in range(len(m2)):
                print 'i='+str(i)
                print 'j='+str(j)
                print 'k='+str(k)
                mat[i][j]+=m1[i][k]*m2[k][j]
                print str(m1[i][j])+' * '+str(m2[k][j])+' => '+str(mat[i][j])
    return mat

#a=new_matrix(4,3)
#b=new_matrix(2,4)

a=new_matrix(3,2)
b=new_matrix(2,3)

a[0][0]=1
a[0][1]=2
a[0][2]=3
a[1][0]=4
a[1][1]=5
a[1][2]=6

b[0][0]=7
b[0][1]=8
b[1][0]=9
b[1][1]=10
b[2][0]=11
b[2][1]=12

print 'matrix 1:'
print_matrix(a)
print 'matrix 2:'
print_matrix(b)

#matrix_mult(a,b)
print_matrix(matrix_mult(a,b))
