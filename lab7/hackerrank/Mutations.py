def mutate_string(string, position, character):
    l = ''
    for i in range(0, len(string)):
        if i != position:
            l += string[i]
        else:
            l += character
    return l