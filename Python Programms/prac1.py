
try:
    def fibi(n):
        a, b = 0, 1
        l=[]
        for i in range(n):
            l.append(a)
            a, b = b, a + b    
        return l,a
except Exception,e:
    print e

"""m=int(raw_input("enter the range for fibonacci series")) 
x,y=fibi(m)
print "fibbonacci series is %s" %x
print "total is %s" %y"""



try:
    def fact(n):
        if n==1:
            return n

        else:
            print b
            return n*fact(n-1)
except Exception, e:
    print e

#n=int(raw_input("enter the range"))
#x=fact(n)
#print "factorial of %d is %d" %(n,x)



try:
    def even(n,p):
        l=[]
        for i in range(n):
            if i%p==0:
                l.append(i)
        return l
except Exception,e:
    print e
    
#x=even(10,4)
#print x


m=[2,3,5,6,4,1,9,7,8]
n=sorted(m)
print n
print reversed(n)

l=[1,2,3,4,5,6,7,8,9]
x=cmp(l,n)
print x




        


            

             





