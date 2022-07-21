# def pyramid(n):
#     k=n-2
#     for i in range(1,n+1):
        
#         for j in range(1,k+1):
#             print(end=" ")
#         k=k-1
#         for j in range(1,i+1):
#             print("* ",end="")
#         print("\r")
# num=int(input("Enter the number: "))
# # pyramid(num)
# def inverse_pyramid(n):
#     k=n-2
#     for i in range(n,-1,-1):
        
#         for j in range(k,-1,-1):
#             print(end=" ")
#         k=k+1
#         for j in range(0,i+1):
#             print("* ",end="")
#         print("\r")
# num=int(input("Enter the number: "))
# inverse_pyramid(num)

# def right_star(n):
#     k=n-2
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* ",end="")
#             print(end=" ")
#         print("\r")
#     for i in range(n,-1,-1):
#         for j in range(0,i+1):
#             print("* ",end="")
#             print(end=" ")
#         print("\r")
# num=int(input("Enter the number: "))
# right_star(num)

# def left_star(n):
#     k=2*n-2
#     for i in range(1,n):
#         for j in range(1,k):
#             print(end=" ")
#         k=k-2
#         for j in range(1,i+1):
#             print(" *",end="")
#         print("\r")
#     k=-1
#     for i in range(n-1,-1,-1):
#         for j in range(k,0,-1):
#             print(end=" ")
#         k=k+2
#         for j in range(0,i+1):
#             print(" *",end="")
#         print("\r")
# # num=int(input("Enter the number: "))
# left_star(5)



# def hourglass(n):
#     k=n-2
#     for i in range(n,-1,-1):
#         for j in range(k,-1,-1):
#             print(end=" ")
#         k=k+1
#         for j in range(1,i+1):
#             print("* ",end="")
#         print("\r")
#     k=n*2-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k- 1
#         for j in range(0,i+1):
#             print("* ",end="")
#         print("\r")
# # num=int(input("Enter the number: "))
# hourglass(5)



# def leftrct(n):
#     k=n-2
#     for i in range(1,n):
#         for j in range(1,i+1):
#             print("* ",end=" ")
#         print("\r")
    
# # num=int(input("Enter the number: "))
# leftrct(5)

# def downlrct(n):
#     k=n-2
#     for i in range(n,-1,-1):
#         for j in range(i,-1,-1):
#             print("* ",end=" ")
#         print("\r")
    
# # num=int(input("Enter the number: "))
# downlrct(5)

# def rightrct(n):
#     k=2*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k-2
#         for j in range(1,i+1): 
#             print("* ",end="")
#         print("\r")
    
# # num=int(input("Enter the number: "))
# rightrct(5)
# def uprct(n):
#     k=2*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k-1
#         for j in range(i,-1,-1):
#             print("* ",end="")
        
#         print("\r")
#     k=n-2
#     for i in range(n,-1,-1):
#         for j in range(k,0,-1):
#             print(end=" ")
#         k=k+1
#         for j in range(i,-1,-1):
#             print("* ",end="")
        
#         print("\r")

    
# # num=int(input("Enter the number: "))
# uprct(5)


# def leftrct(n):
#     for i in range(n):
#         for j in range(n):
#             if i+j==2 or i-j==2 or i+j==6 or   j-i==2:
#                 print("*",end=" ")
#             print(end=" ")
#         print()
    
# # num=int(input("Enter the number: "))
# leftrct(5)


# def number(n):
#     x=0
#     for i in range(n):
#         x+=1
#         for j in range(0,i+1):
#             print(x,end=" ")
#         print("\r")
    
# # # num=int(input("Enter the number: "))
# number(5)

# Passcal traingle

def number(n):
    for i in range(n):
        for j in range(0,i+1):
            print(function(i,j),end=" ")
        print()
def function(n,k):
    res=1
    if (k>n-k):
        k=n-k
    for i in range(0,k):
        res*=(n-i)
        res//=(i+1)
    return res
# # num=int(input("Enter the number: "))
number(15)

