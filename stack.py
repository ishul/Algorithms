import time
from collections import deque

start = time.time()

stack = deque([1, 2, 3])
stack.append(4)
stack.append(5)
value = stack.pop()
print(stack, value)

end = time.time()

print(end-start)
