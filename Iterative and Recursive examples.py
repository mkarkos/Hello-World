def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    x = 0
    while aStr > '':
        x += 1
        aStr = aStr[:-1]
    return x
    

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
    x = 0 
    if aStr == "":
       x = 0
    else:
       x += 1 + lenRecur(aStr[1:])
    return x
  

def lenRecura(aStr):
    if aStr == '':
         return 0
    else:
         return 1 + lenRecur(aStr[1:])
print lenRecura("bobby") 