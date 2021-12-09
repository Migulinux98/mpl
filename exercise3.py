

def BubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


list = [54,26,93,17,77,31,44,55,20]
print("the unsorted list:", list)
print("the sorted list", BubbleSort(list))