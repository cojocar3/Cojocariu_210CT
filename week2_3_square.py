def square(x):
    last_s = None 
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j*j == i :
                last_s = i 
    print (last_s)
