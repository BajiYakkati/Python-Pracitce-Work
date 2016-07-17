def test(*args, **kargs):
    print args
    print kargs
    
test([1,2,3,4,5],25,30,50,6,7,{"a":2,"b":3})
