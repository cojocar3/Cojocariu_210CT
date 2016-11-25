import random
order = int(input("Matrix order: "))
mat1 = []
mat2 = []

for i in range(0,order):        # create a loop that fill the list with lists
    mat1.append([])
    mat2.append([])
    for j in range (0,order):   # fill the list with random numbers from a range
        mat1[i].append(random.randint(1,3))
        mat2[i].append(random.randint(1,3))
      
def add (mat1,mat2):
    mat_add = []
    for i in range(len(mat1)):     # for every list in mat1 creates a new list where the sum will be
        mat_add.append([])
        for j in range(len(mat1[0])):   # adds to list the sum of elements from the 2 matrix
         mat_add[i].append(mat1[i][j]+mat2[i][j])   
    return(mat_add)

def sub(mat1,mat2):
    mat_sub = []
    for i in range(len(mat1)):      # for every list in mat1 creates a new list where the substraction result will be placed
        mat_sub.append([])
        for j in range(len(mat1[0])):
            mat_sub[i].append(mat1[i][j]-mat2[i][j]) # adds to list the substraction of elements from the 2 matrix
    return(mat_sub)

def mult(mat1,mat2):
    mat_mult=[]
    for i in range(len(mat1)):
        mat_mult.append([])
        for j in range(len(mat1)):
            x = 0
            for k in range(len(mat1[0])):
                x = x+mat1[i][k]*mat2[k][j]
            mat_mult[i].append(x)
    return mat_mult
def mult_by_nr(nr,mat1):
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            mat1[i][j] = nr*mat1[i][j]
    return mat1
R = mult(mat1,mat2)
P = add(mat1,mat2)
Q = mult_by_nr(2,P)
A = sub(R,Q)

print (mat1)
print (mat2)
print (A)
##print(add(mat1,mat2))
##print (sub(mat1,mat2))
##print (mult(mat1,mat2))
##print (mult_by_nr(10,mat1))
