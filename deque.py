from collections import deque

dq = deque([1, 6, 2, 3, 4, 5])
dq.extend([16, 17])
dq.extendleft({'first':11, 'second':12})

dq.clear()
print(dq)
