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
print_matrix(n);


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
    pass

