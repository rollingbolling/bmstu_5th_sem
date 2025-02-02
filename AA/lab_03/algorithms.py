def locate(source: list[int], x: int) -> (int, int):
    index = -1
    compare = 0
    
    for i in range(len(source)):
        compare += 1
        if source[i] == x:
            index = i
            break
        
    return index, compare

def bin_locate(source: list[int], x: int) -> (int, int):
    index = -1
    compare = 0
    
    left = 0
    right = len(source) - 1
    while left <= right:
        compare += 1
        middle = (left + right) // 2
        if source[middle] == x:
            index = middle
            break
        elif source[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
            
    return index, compare        
