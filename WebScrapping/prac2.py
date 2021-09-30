list1 = [int(x) for x in input().split(',')]
list2 = [int(x) for x in input().split(',')]
if len(list1)==len(list2):
    for i in range(1,len(list1),2):
        list1[i]=list1[i]*2
    print('Updated list2',end='')

    print(list1)
else:
    print('The length of the lists are not equal')


