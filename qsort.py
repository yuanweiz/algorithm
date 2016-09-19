import base
def partition (arr,start,end):
    if (end-start <=1):
        return  #Oops
    key = arr[start]
    p=q=start+1
    while q < end:
        if (arr[q] < key):
            arr[q],arr[p]=arr[p],arr[q]
            p,q=p+1,q+1
        else:
            q = q+1
    arr[start],arr[p-1] = arr[p-1],arr[start]
    return p-1

def helper(arr,start,end):
    if end-start <=1:
        return;
    mid = partition (arr,start,end)
    helper(arr,start,mid)
    helper(arr,mid+1,end)

def qsort (arr):
    helper(arr,0,len(arr))

if __name__ == '__main__':
    for i in range (10):
        arr = base.genlist ()
        qsort (arr)
        if base.isSorted(arr) :
            print "Correct!,result is", arr
        else:
            print "Wrong!,result is", arr
