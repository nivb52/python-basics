list1 = [1,2,3]
list2 = [10,20,30]
print('zip function')
# WE WANT TO COMBINED ITEM EACH BY EACH
# LIKE (a , 1 ,10 )
print(list(zip(list1,list2)))
print(list(zip('abc',list1,list2)))