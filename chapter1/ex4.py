def encode(s):
    """
    Run length encoding
    (str) -> str
    
    >>> encode('BWWWWWBWWWW')
    '1B5W1B4W'
    """
    ret = ''
    grpSize = 0
    grpChar = None
    for ch in s:
        if ch != grpChar:
            if grpSize:
                ret += "{}{}".format(grpSize, grpChar)
            grpSize = 1
            grpChar = ch
        else:
            grpSize += 1
    if grpSize:
        ret += "{}{}".format(grpSize, grpChar)
        
    return ret


def decode(s):
    """
    Run length decoding
    (str) -> str
    
    >>> decode('1B5W1B4W')
    'BWWWWWBWWWW'
    """
    ret = ''
    sizeStr = ''
    for ch in s:
        if ch.isalpha():
            if sizeStr:
                ret += ch * int(sizeStr)
                sizeStr = ''
        else:
            sizeStr += ch
    
    return ret
    
    
if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
