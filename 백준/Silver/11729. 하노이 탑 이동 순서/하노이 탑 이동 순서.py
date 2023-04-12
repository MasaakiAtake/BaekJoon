def hanoi(n, fr, tmp, to):

    if(n==1):
        print("%s %s" % (fr, to))
    else:
        hanoi(n-1,fr,to,tmp)
        print("%s %s" % (fr,to))
        hanoi(n-1,tmp,fr,to)
a = int(input())
print(2**a-1)
hanoi(a,"1","2","3")