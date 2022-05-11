#Return the number (count) of vowels in the given string.

#We will consider (a, e, i, o, u) as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):    
    v=0
    for n in sentence:
        if n =="a" or n=="e" or n=="i" or n=="o" or n=="u":
            v+=1
        else:
            continue
    return v 