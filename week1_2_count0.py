nr = int(input("Insert number: ")) # user insert number 

x = 1 
for i in range(1,nr+1):
    x *=i
    if nr == 0:
        x = 1
print ("There are "+str(nr//5)+" 0s at the end of the number")
print(x)
