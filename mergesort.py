#!/usr/bin/python2
import copy
import base.genlist as genlist

def merge (dst,src,s1,e1,s2,e2):
    i = s1
    while ( s1 < e1 ):
        if (s2 == e2 ):
            dst[i:i+e1-s1]=src[s1:e1]
            break;
        if  src[s1] < src[s2] :
            dst[i]=src[s1]
            s1 = s1+1
        else:
            dst[i] = src[s2];
            s2 = s2+1
        i = i + 1
    dst[i:i+e2-s2]=src[s2:e2] #no need to predicate

def mergesort(arr):
    #buff = [ i for i in arr] #deep copy
    buff = [ 0 for i in arr] #deep copy
    mergesort_helper (arr,buff,0, len(arr) )

def mergesort_helper (arr,buff,s,e):
    if ( s == e-1 ):
        return; 
    mid = (s+e)/2
    mergesort_helper(arr,buff,s,mid)
    mergesort_helper(arr,buff,mid,e)
    buff[s:e] = arr[s:e]
    merge (arr,buff, s,mid,mid,e );


    
if __name__ == "__main__":
    arr = genlist()
    mergesort(arr)
    if not isSorted(arr):
        print "Wrong! Result is:\n",arr
    else:
        print "Correct! Result is:\n",arr
