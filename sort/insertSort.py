def insertSort(list):
    for i in range(1,len(list)):
        print('i=',i)
        for j in range(i,-1,-1):
            if(list[j]<list[j-1]):
                temp=list[j-1]
                list[j-1]=list[j]
                list[j]=temp
            else:
                break

            print(list)

list=[-1,1,7,3,4,2,5]
print(list)
insertSort(list)