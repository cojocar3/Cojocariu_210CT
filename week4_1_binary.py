listA = [1,2,4,5,6,7,11,13,17]      
interval_start = int(input("Insert start point value for the interval: "))
interval_stop = int(input("Insert stop point value for the interval: "))

def binary (listA,interval_start,interval_stop):
    start = 0
    stop = len(listA)-1
    if len(listA)==0:          #if the list is empty or the value is not in the interval print false 
        print ('False')
    else:
        mid=(start+stop)//2
        if listA[mid] in range(interval_start,interval_stop):   #if the mid point is in the interval print true
            print ('True')
        else:
            if interval_stop<listA[mid]:                    #if the interval is smaller than mid point , remove any value higher than the mid point , recall the function
                return binary(listA[:mid],interval_start,interval_stop)
            else:
                return binary(listA[mid+1:],interval_start,interval_stop)# if the interval is higher than the mid point , remove any value smaller than the mid point , recall the function.
binary(listA,interval_start,interval_stop)
