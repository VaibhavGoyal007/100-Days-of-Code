T = int(input())
if 1 <= T <= 1000:
    for i in range(0,T):
        N = int(input())
        if 1 <= N <= 1000000:
            rev = 0
            while(N != 0):
                temp = N % 10
                N = N // 10
                rev = rev*10 + temp
            print(rev)
