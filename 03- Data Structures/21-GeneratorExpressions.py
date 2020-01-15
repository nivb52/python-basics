# //    21- Generator Expressions
from sys import getsizeof

veryBigValue = (x * 2 for x in range (10000))

# THIS GEN DONT HAVE LEN() {length}  : 
print('gen size in bytes: ', getsizeof(veryBigValue) )
print('compared too : ')

unEfficientValues = [ i * 2 for i in range(10000)]
print('gen size in bytes: ', getsizeof(unEfficientValues) )



