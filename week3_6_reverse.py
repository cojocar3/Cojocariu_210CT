word = input("Insert sentence: ")
w_list = word.split(" ")
out = []
def reverse(w_list):
    while w_list != []:
        for i in range(len(w_list)-1,-1,-1):
            out.append(w_list[i]+' ')
            w_list.remove(w_list[i])
reverse(w_list)
print (''.join(out))
        
