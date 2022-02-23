def largest_product(series,size):
    if size>len(series):
        raise ValueError("span must be smaller than string length")
    elif size<0:
        raise ValueError("span must not be negative")
    elif size==0:
        return 1
    elif (not series.isdecimal()):
        raise ValueError("digits input must only contain digits")
    max_product=0
    for x in range(0, len(series)-size+1):
        current_product=1
        for y in series[x:x+size]:
            current_product*=int(y)
        if current_product>max_product:
            max_product=current_product
    return max_product