#Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, 
#or after the addition.

#The binary number returned should be a string.

def add_binary(a,b):
    x=a+b
    y=""
    while x>2:
        if x%2==0:
            x//=2
            y+="0"
        else:
            x//=2
            y+="1"
    if x==2:
        y+="01"
    else:
        y+="1"
    y="".join(reversed(y))
    return y