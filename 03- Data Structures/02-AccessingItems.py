nums = [1,2,3,4,5,6]
print ("first item: ",nums[0])
print ("last item: ",nums[-1])

nums[0]='A'
print ("first item: ",nums[0])

numbers = list (range(20))
# // slice 
print(numbers[:4]) #from 0 to 3

# [start:end]:step : 
# example : 
# this mean give me all list with is the step of 2 : 
print (numbers[::2])
# step of 3 :  
print(numbers[::3])