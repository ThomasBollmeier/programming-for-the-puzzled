def pleaseConformOnepass(caps):
    
    def printMessage(start, end):
        if end > start:
            print('People in positions', start, 'through', end, 'flip your caps')
        else:
            print('Person at position', start, 'flip your cap')
            
    if not caps:
        return
    
    first = -1
    for i in range(len(caps)):
        if caps[i] != 'H':
            first = i
            break
    if first < 0:
        return
            
    start = -1
    caps = caps + [caps[first]]
    for i in range(first+1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] not in [caps[first], 'H']:
                start = i
            else:
                if start > 0: 
                    printMessage(start, i-1)
                    start = -1


if __name__ == "__main__":

    caps = list('FFBHBFBBBFHFF')
    
    pleaseConformOnepass(caps)