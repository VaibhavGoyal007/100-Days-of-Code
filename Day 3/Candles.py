n = int(input())
count = 0
if 1 <= n <= 100000:
    ar = [int(x) for x in input().split(" ")]
    if 1 <= len(ar) <= 10000000:
        max_ = max(ar)
        for i in range(len(ar)):
            if ar[i] == max_:
                count += 1
        print(count)
    else:
        print("Candles are more than expected....")
else:
    print("Cannot put {} candles on the cake".format(n))
