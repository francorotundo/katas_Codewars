#Escribe una función que tome una cadena de paréntesis y determine si el orden de los paréntesis es válido. 
# La función debería regresar truesi la cadena es válida y falsesi no es válida.

#Restricciones
#0 <= input.length <= 100

#Junto con los paréntesis de apertura ( () y cierre ( )), la entrada puede contener cualquier carácter ASCII válido.
#Además, la cadena de entrada puede estar vacía y/o no contener ningún paréntesis. No trate otras formas de corchetes
#como paréntesis (p. ej . [], {}, <>).

def valid_parentheses(string):
    for i in string: 
        if i != '(' and i != ')': string = string.replace(i, '')
    while '()' in string: string= string.replace('()','')
    return len(string)==0

print(valid_parentheses('hi(hi)'))