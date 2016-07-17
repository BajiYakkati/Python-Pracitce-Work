questions=["name","height","weight"]
l=[]
s={}

for i in range(1,3):
    x=[raw_input("enter values of name, Height, weight")]
    l.append(x)
print l
        
"""n=tuple(l)
print type(n)
print n"""

for j in l:
   for i in j:
       print i
       for q,a in zip(questions,i):
           print "what is your {0}, it is {1}" .format(q,a)
     
     

     
