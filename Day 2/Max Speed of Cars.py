T = int(input())
if 1 <= T <= 100:
    for i in range(0,T):
        count = 1
        N = int(input())
        if 1 <= N <= 10000:
            l = [int(x) for x in input().split()]
            if N == 1 and len(l) == N:
                print(count)
            elif len(l) > N:
                print("No. of cars you entered are more than the expected value")
            elif len(l) < N:
                print("No. of cars you entered are less than the expected value")
            else:
                for j in range(1,len(l)):
                    flag = 0
                    for k in range(0,j):
                        if l[j] > l[k]:
                            flag = 0
                            break
                        else:
                            flag = 1
                    if flag == 1:
                        count += 1
                print(count)
            
                
