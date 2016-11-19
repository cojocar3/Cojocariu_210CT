def vow(s):                 
    if s == "":             #base case , if the string is empty , return the string
        return s
    else:
        if s[0] in 'aeiou':     # if the index is a vowel, call the function from the next index
            return vow(s[1:])   
        else:                   # if the index is not a vowel return , keeps the letter and recalls the function for the next index
            return s[0]+vow(s[1:])
