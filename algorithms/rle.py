vvod = input('in: ')
if len(vvod) > 1:
    count = 1
    prev = ''
    lst = []
    for i in vvod:
        if i != prev:
            if prev:
                entry = ''
                entry = str(count) + prev
                lst.append(entry)
            count = 1
            prev = i
        else:
            count += 1
    else:
        entry = str(count) + i
        lst.append(entry)
    ones = ''.join(lst)
    x = ''
    for i in ones:
        if i != '1':
            x = x + i
    print('out: ', x)
else:
    print('out: ', vvod)