import random  
inp  = input("Insert numbers: ") # user input numbers that needs to be shuffled

inp_list = inp.split(",") # transform the input into list
out_list = []             # create a list where the shuffled numbers will be stored  

while inp_list != []:     # execute loop until the input list is empty
    ran = random.randint(0,len(inp_list)-1) # choose a index from the list which store the inserted numbers
    out_list.append(inp_list[ran])          # adds the value of the index to the list which store the shuffled numbers
    inp_list.remove(inp_list[ran])          # remove the value of the index from the first list 
    
print (out_list)                            # print the shuffled list
