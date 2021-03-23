#import NM
import numpy

print("in pycharm",__name__)


def testArg(a,b,*arg,**kw,):
    print(a,b,kw,arg)


testArg(1,2,123,4,5,6,city='asd')

a = [-1029303030,2,3]
b = [-1029303030,2,3]

print(id(-1000000))
print(id(-1000000))
print(id(a))
print(id(b))

rr = 1+2J
print(rr)

print(numpy.conjugate([1,2,3]))