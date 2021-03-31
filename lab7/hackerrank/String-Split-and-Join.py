def split_and_join(line):
    l = line.split()
    ans = ''
    for i in range(0, len(l)-1):
        ans += l[i] + '-'
    ans += l[len(l)-1]
    return ans
