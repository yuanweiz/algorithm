import random
def genlist( ):
    sz = random.randrange(100);
    return [ random.randrange(100) for i in xrange(sz) ]

#def trace(func, *args):
#    ret = func(*args)
#    print 'In', func.func_name, args ,'=',ret
#    return ret

def isSorted (arr ):
    for i in xrange(1,len(arr)):
        if (arr[i] < arr[i-1]):
            return False
    return True;

