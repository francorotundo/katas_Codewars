# def valid_braces(string):
#     cor = 0
#     par = 0
#     lla = 0
#     for i in string:
#         if i == '[':
#             cor+=1
#         elif i == ']':
#             cor-=1
#         elif i == '{':
#             lla+=1
#         elif i == '}':
#             lla-=1
#         elif i == '(':
#             par+=1
#         elif i == ')':
#             par-=1
#         else:
#             return False
    
#     for x in range(0, len(string)-1):
#         if string[x] == ']':
#             if string[x-1] == '[' or string[x-1] == ']' or string[x-1] == '}' or string[x-1] == ')':
#                 continue   
#             else: return False 

#         elif string[x] == '[':
#             if string[x+1] == ']' or string[x+1] == '[' or string[x+1] == '{' or string[x+1] == '(':
#                 continue   
#             else: return False        

#         elif string[x] == ')':
#             if string[x-1] == '(' or string[x-1] == ']' or string[x-1] == '}' or string[x-1] == ')':
#                 continue
#             else:
#                 return False
        
#         elif string[x] == '(':
#             if string[x+1] == ')' or string[x+1] == '[' or string[x+1] == '{' or string[x+1] == '(':
#                 continue   
#             else: return False  

#         elif string[x] == '}':
#             if string[x-1] == '{' or string[x-1] == ']' or string[x-1] == '}' or string[x-1] == ')':
#                 continue
#             else:
#                 return False
        
#         elif string[x] == '{':
#             if string[x+1] == '}' or string[x+1] == '[' or string[x+1] == '{' or string[x+1] == '(':
#                 continue   
#             else: return False  

#     if cor == 0 and lla == 0 and par == 0 and (string[0] == '[' or string[0] == '{' or string[0] == '(') and (string[-1] == ']' or string[-1] == '}' or string[-1] == ')'):
#         return True
#     else:
#         return False
#---------------------------------------------------------------------------------------------------------------------
#Uso de replace
def valid_braces(string):
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    return string == ''

#---------------------------------------------------------------------------------------------------------------------
# def valid_braces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0  

print(valid_braces("())({}}{()][]["))

