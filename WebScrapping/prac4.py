n = input()
num = [int(x) for x in input().split()]
for i in range(len(num)-1, -1, -1):
    print(num[i], end='')
    if i != 0:
        print(' ', end='')
    else:
        print()
