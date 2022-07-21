import  numpy as np


def what_matrix():
    query=input("Entter what you want to do : ").lower()
    m=int(input("Enter nubmer of row  of your matrix: "))
   
    n=int(input("Enter number of column of your matrix: "))
    

    a=np.zeros((m ,n)).reshape(m,n)
    print("Enter the element of matrix")
    for i in range(m):
        for j in range(n):
            a[i,j]=int(input())
        
    # Identity(a,m,n)     
       
    
    if m==n and query=="transpose":
        print(a)
        c=a.copy()
        transpose(c,m,n)
    elif query=="matrix multipication":
        m2=int(input("Enter nubmer of row  of your 2nd matrix: "))  
        n2=int(input("Enter number of column of your 2nd matrix: "))
        d=np.zeros((m2,n2)).reshape(m2,n2)
        print("Enter the element of matrix")
        for i in range(m2):
            for j in range(n2):
                d[i,j]=int(input())
        if m==m2 and n==n2:
            matadd(a,d,m,n)               
            
        
    
def Identity(mat,m,n):
    for i in range(m):
        for j in range(n):
            if i==j:
               if mat[i][j]==1:
                   continue       
            else:
                if mat[i][j]==0:
                       continue
    
def transpose(mat,m,n):
    temp=np.zeros((m,n)).reshape(m,n)  
    for i in range(m):
        for j in range(n):
            temp[i][j]=mat[j][i]
    print("Your transpose matrix is :")
    print(temp)    

def matmul(mat1,mat2,m,n):
    temp=np.zeros((m,n)).reshape(m,n)  
    for i in range(m):
        for j in range(n):
            temp[i][j]=mat1[i][j]
    print("Your transpose matrix is :")
    print(temp)    
def matadd(mat1,mat2,m,n):
    temp=np.zeros((m,n)).reshape(m,n)  
    for i in range(m):
        for j in range(n):
            temp[i][j]=mat1[i][j]+mat2[i][j]
    print("Your addation matrix is :")
    print(temp)    
what_matrix()        
