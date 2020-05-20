def running_median(stream):
    output = []
    sort = []
    for x in range(len(stream)):
        if x == 0:
            output.append(stream[x])
            sort.append(stream[x])
        elif (x+1) % 2 == 0:
            sort.append(stream[x])
            sort = sorted(sort)
            output.append((sort[x//2] + sort[x//2 + 1])/2)
        else:
            sort.append(stream[x])
            sort = sorted(sort)
            output.append(sort[x//2])
    print(output)

running_median([2,1,4,7,2,0,5])
