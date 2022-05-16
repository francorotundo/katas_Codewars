#ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
#ROT13 is an example of the Caesar cipher.

#Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special 
#characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet 
#should be shifted, like in the original Rot13 "implementation".

#Please note that using encode is considered cheating.

def rot13(message):
    msj=''
    for ch in message:
        if 65<=ord(ch)<=90:
            if ord(ch)>=78: msj += chr(ord(ch) -13)
            else: msj += chr(ord(ch) +13)
        elif 97<=ord(ch)<=122:
            if ord(ch)>=110: msj += chr(ord(ch) -13)
            else: msj +=  chr(ord(ch) +13)
        else:
            msj += ch
    return msj

print(rot13('Pbqrjnef12'))