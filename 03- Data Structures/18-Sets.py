nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4]
print(nums)
print('using SETS : only 1 value of each! ')
uniques = set(nums)
print(uniques)

a = {1,3}
print(a , 'defined only 1 & 3 by {1,3}')
print(' === ')
a.add(53)
a.add(4)
a.add(5)
a.add(7)
a.add(0)
a.add(2)
a.remove(1)
print(a, ' ... len(): ', len(a))


print('a',a)
print('uniques',uniques)
print(' WHERE SETS ARE SHINE')
print(' =============')
print(' =============')
# union : operetor |
print('    | => union: ', a | uniques)
# have diffrance : operetor -
print('    - => diffrances : ',a - uniques)
# have both : operetor &
print('    & => both have: ', a & uniques)
# only in 1 sets : operetor ^
print('    ^ => only in 1 set :',a ^ uniques)

print(' =============')
print(' =============')

if 1 in a :
    print('1 is in set a')
print ('1 is no in set a ')