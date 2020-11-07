import time
start_time = time.time()

inp = input('in: ')
if len(inp) > 1:
    count = 1
    prev = ''
    lst = []
    for i in inp:
        if i != prev:
            if prev:
                # entry = ''
                entry = str(count) + prev
                lst.append(entry)
            count = 1
            prev = i
        else:
            count += 1
    else:
        # entry = str(count) + i
        entry = str(count) + prev
        lst.append(entry)
    ones = ''.join(lst)
    # x = ''
    # for i in ones:
    #    if i != '1':
    #        x = x + i
    print('out: ', ones)
else:
    print('out: ', inp)

print("--- %s seconds ---" % (time.time() - start_time))
