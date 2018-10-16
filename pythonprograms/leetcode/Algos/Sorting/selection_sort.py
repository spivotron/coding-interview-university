def selectionSort(lst):
    for fillslot in range(len(lst)-1, 0 , -1): # 1. Keep going through the list
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if lst[location] > lst[positionOfMax]: # 2. Find the newest max
                positionOfMax = location
        lst[fillslot], lst[positionOfMax] = lst[positionOfMax], lst[fillslot]
        # temp = lst[fillslot]
        # lst[fillslot] = lst[positionOfMax]
        # lst[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)