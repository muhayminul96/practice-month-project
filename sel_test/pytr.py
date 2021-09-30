m = 36
n = 1
arr = []
while (m > -5):
    if n < 40:
        arr.append(n)
        n = n*2 + 3
    else:
        n = n - m
        m -= 10
        continue
print(arr)
