input_list = [int(x) for x in input().split(',')]
prime_list=[]
for num in input_list:
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            prime_list.append(num)


    else:
        continue
print("Inputlist", end='')
print(input_list)
print('prime list',end='')
print(prime_list)

total = sum(prime_list)

if total > 1:

    for i in range(2, total):
        if (total % i) == 0:
            print('Just another normal day!!!')
            break

    else:
        print("It’s a miracle!!!")


else:
    print('Just another normal day!!!')
