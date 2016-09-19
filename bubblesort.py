import base
def bubblesort(arr):
    for i in range (len(arr)-1):
        for j in range (len(arr)-1 , i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr



if __name__ == '__main__':
    for i in range (10):
        arr = base.genlist ()
        arr = bubblesort (arr)
        if base.isSorted(arr) :
            print "Correct!,result is", arr
        else:
            print "Wrong!,result is", arr
