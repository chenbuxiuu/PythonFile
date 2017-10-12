def selectionSort(list):
    for i in range(len(list)-1):
        minNum=i
        for j in(i+1,len(list)-1):
            if list[j]<list[minNum]:
                minNum=j
        temp=list[i]
        list[i]=list[minNum]
        list[minNum]=temp
        print(list)

list=[3,4,8,7,5]
print(list)
selectionSort(list)