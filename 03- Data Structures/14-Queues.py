# technically we can use list
# but if we use large list or queue 
# we can see preomance issues

from collections import deque
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
queue.popleft()
print('after *popleft*',queue)
print(' use: *if not queue* : to check if empty ')
if not queue:
    print("empty")