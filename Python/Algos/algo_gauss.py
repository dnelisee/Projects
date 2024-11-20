def Remontee(A, b, X) : 
    n = len(b)-1
    X[n] = b[n]/A[n][n] 
    for i in range(n-1, -1, -1) : 
        X[i] = b[i]
        for j in range(i+1,n+1) :
            X[i] -= A[i][j]*X[j] 
        X[i] /= A[i][i] 
    return X 

def pivot_partiel(A, b, k) : 
    n = len(b)-1
    i_max = k 
    for i in range(k+1, n+1) : 
        if abs(A[i][k]) > abs(A[i_max][k]) : 
            i_max = i 
    
    if i_max != k : 
        b[i_max], b[k] = b[k], b[i_max] 
        for j in range(k, n+1) : 
            A[i_max][j], A[k][j] = A[k][j], A[i_max][j] 

    return A, b

def Elimination(A, b) :
    n = len(b)-1 
    for k in range(0,n) : 
        A, b = pivot_partiel(A, b, k) 

        for i in range(k+1, n+1) : 
            l = A[i][k]/A[k][k] 
            b[i] -= l*b[k] 
            for j in range(k+1, n+1) : 
                A[i][j] -= l*A[k][j] 
    return A, b 

def Gauss(A, b, X) : 
    A, b = Elimination(A, b)
    X = Remontee(A,b,X) 
    return X 

# example 
A = [[1,1,1], [1,-1,-1], [1,-1,1]]
b = [3,-1,1] 
X = [0,0,0] 
X = Gauss(A, b, X) 
print(X)

