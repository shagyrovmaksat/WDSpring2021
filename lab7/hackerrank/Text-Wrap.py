def wrap(string, max_width):
    l = ''
    for i in range(0,len(string),max_width):
        if(i + max_width - 1 <= len(string)-1):
            l += string[i:i+max_width] + '\n'
        else:
            l += string[i:]
    return l