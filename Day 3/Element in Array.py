array = [int(x) for x in input().split(" ")]
n = int(input())
try:
    array.index(n)
    print(array.index(n))
except:
    for i in range(len(array)):
        if n < array[i]:
            print(i)
            break      
    print(len(array))
