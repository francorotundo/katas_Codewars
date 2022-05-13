#The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation 
# being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the 
# closest valid value.

#Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

def rgb(r, g, b):
    hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    color = {'r': r, 'g': g, 'b': b}
    for key,value in color.items():
        if value < 0:
            color[key] = '00'
        elif value >= 0 and value<=255:
            x1 = value%16
            x2 = value//16
            color[key] = hex[x2] + hex[x1]
        else:
            color[key] =  'FF'
    return color['r']+ color['g'] + color['b']    



print(rgb(-20, -5, 300))
        


            