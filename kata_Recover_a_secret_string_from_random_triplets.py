#There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

#A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. 
#"whi" is a triplet for the string "whatisup".

#As a simplification, you may assume that no letter occurs more than once in the secret string.

#You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient 
# information to deduce the original string. In particular, this means that the secret string will never contain letters that do 
# not occur in one of the triplets given to you.

def recoverSecret(triplets):
    secret = []
    for triplet in triplets:
        x, y, z = triplet

        if x not in secret:
            secret.insert(0, x)
        if y not in secret:
            secret.insert(secret.index(x), y)
        if y in secret and secret.index(y) < secret.index(x):
            secret.pop(secret.index(y))
            secret.insert(secret.index(x)+1, y)
        if z not in secret:
            secret.insert(secret.index(y), z)
        if z in secret and secret.index(z) < secret.index(y):
            secret.pop(secret.index(z))
            secret.insert(secret.index(y)+1, z)
        
    return ''.join(secret)


triplets = [['t','u','p'],['w','h','i'],['t','s','u'],['a','t','s'],['h','a','p'],['t','i','s'],['w','h','s']]


print(recoverSecret(triplets))

# def recoverSecret(triplets):
#     letras= []
#     numero_de_letras = len({ch for triplet in triplets for ch in triplet})

#     while len(letras)< numero_de_letras:
#         for i, triplet in enumerate(triplets):
#             for j, ch in enumerate(tuple(triplet)):
#                 if ch not in letras:
#                     if i==0:
#                         letras.append(ch)
#                     else: 
#                         if j<2 and triplet[j+1] in letras: 
#                             letras.insert(letras.index(triplet[j+1]),ch)

#     return ''.join(letras)

# def recoverSecret(triplets):
#     secret = []
#     i = 0
#     c = 0
#     while c<len(triplets)-1: 
#         x, y, z = triplets[i] 
        
#         if x in secret and y in secret and z in secret:
#             c += 1
        
#         else:
#             if i==0:
#                 secret = [x, y, z]
#             else:
#                 if x not in secret and y in secret: 
#                     secret.insert(secret.index(y),x)
#                 if y not in secret and z in secret:
#                     secret.insert(secret.index(z),y)
#                 if z not in secret and y in secret:
#                     secret.append(z) 

#         if i<len(triplets)-1: i+=1
#         else: i=0

#     return ''.join(secret)