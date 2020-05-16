T = int(input())
if 1 <= T <= 5:
    for i in range(0,T):
        N = input()
        if sorted(N.lower()) == sorted("helloworld"):
            print("Yes")
        else:
            print("No")
