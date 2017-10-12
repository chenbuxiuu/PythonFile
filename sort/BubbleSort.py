def bubbleSort(list):
    for i in range(len(list)-1,-1,-1):
        for j in range(i):
            if list[j]<list[j+1]:
                a=list[j]
                list[j]=list[j+1]
                list[j+1]=a
        print(list)

list=[7,9,1,3,8]
print(list)
bubbleSort(list)

# def fun(n):
#     for i in range(n-1,-1,-1):
#         print(i)

# fun(2)