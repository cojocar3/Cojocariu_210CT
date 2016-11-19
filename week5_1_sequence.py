l = [1,2,3,4,2,3,1,5,6,8,9] #initial list
m = []  #the list where are stored the numbers in ascending order , separated by '/' 
n = []  #the list where are stored the sequence of numbers which have the same length

# the next loop,compare each number, to the next one , if the first number is smaller than the next one
# than , the number will be append to the list , else is added a '/' to separate the sequence of ordered numbers form another.
for i in range(0,len(l)-1): 
    if l[i]<=l[i+1]:
        m.append(l[i])
    else:
        m.append(l[i])
        m.append("/")
m.append(l[len(l)-1])
#remove the '/' from the list and separate each sequence of ordered numbers.        
joined = "".join(str(i)for i in m)
trans =joined.split("/")
#compare the length of each sequence of ordered and keeps the one with the biggest length.
parameter = 0
seq = None
for i in range (0,len(trans)):
    if len(str(trans[i]))>parameter:
        parameter = len(str(trans[i]))
        seq = trans[i]        
#look for more sequence of ordered numbers with the same length        
for i in trans:
    if len(i)==parameter:
        n.append(i)
print (n)
