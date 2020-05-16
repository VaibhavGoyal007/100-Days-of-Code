T = int(input())
if 1 <= T <=100:
    for i in range(0,T):
        str = input()
        l = int(len(str))
        if 2 <= l <=1000:
            if l%2==0:
                if sorted(str[:l//2])==sorted(str[l//2:]):
                    print("Yes")
                else:
                    print("No")
            else:
                if sorted(str[:l//2])==sorted(str[l//2+1:]):
                    print("Yes")
                else:
                    print("No")
        else:
            print("Invalid Input.... Length of the string must be greater than 1")
else:
    print("Error....Number of inputs must be greater than 0")
