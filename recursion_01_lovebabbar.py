# import sys
# sys.setrecursionlimit(2000000000)
# print(sys.getrecursionlimit())


def counting (n):
    if n==1:
        print (1,end="     ")
        return
        
    # print(n,end="     ") ## enable this to print 5 4 3 2 1........n
    counting(n-1)
    print(n,end ="     ") ## enable this to print 1 2 3 4 5..........n
def fact(n):
    if n==1:
        return(1)
    resu=n*fact(n-1)
    return(resu)
def fib(n):
    if n==1 or n==0:
        return(1)
    return(print(fib(n-1)+fib(n-2)))
    
    

n=5
# counting(n)
# print(fact(n))
print(fib(n))