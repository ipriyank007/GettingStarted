import queue

q = queue.PriorityQueue()

q.put((5, 'Get a Haircut'))
q.put((1, 'Make a call'))
q.put((3, 'Buy Slippers'))

for i in range(3):
    print(q.get()[1])