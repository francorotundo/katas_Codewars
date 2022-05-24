# codigo = {'A': 'X', 'B': 'Y','C': 'Z', 'D': 'A', 'E': 'B', 'F':'C', 'G': 'D',
#  'H': 'E', 'I': 'F', 'J':'G', 'K': 'H', 'L': 'I', 'M':'J', 'N':'K', 'O':'L', 
#  'P': 'M', 'Q':'N', 'R': 'O', 'S': 'P', 'T':'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y':'V', 'Z':'W'}
# descifrado = []

# def rot(string):

#     for elemento in string:
#         if elemento in codigo:
#             descifrado.append(codigo[elemento])
#         else:
#             descifrado.append(' ')
#     return ''.join(descifrado)

codigo = {}
descifrado = []

def rot(string):
    for i in range(ord('A'), ord('Z') +1):
        if 68<=i<=90: codigo[chr(i)] = chr(i-3)
        if 65<=i<=67: codigo[chr(i)] = chr(i+23)
    for elemento in string:
        if elemento in codigo:
            descifrado.append(codigo[elemento])
        else:
            descifrado.append(' ')
    return ''.join(descifrado)

print(rot('FXLGDGR HVWD QRFKH'))