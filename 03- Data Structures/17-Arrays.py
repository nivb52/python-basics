# Preformance problem in big numbers? --> Use array

# better for more than 10k


from array import array
# i is for the codetype =  google typecode
# all should be with the same type
numbers = array('i', [1,2,3])
print(numbers)
numbers.insert(0,5)
print('numbers:', numbers)
print('all methods are the same as list')
print("""
for: 
numbers.insert(0,'word')
THE OUTPUT: TypeError: an integer is required (got type str)
""")