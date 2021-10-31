import queue as Q

frontier = Q.PriorityQueue()

frontier._put(3)
frontier._put(4)
frontier._put(1)
frontier._put(2)

x = frontier._get()
print("first pop:",x)
x = frontier._get()
print("second pop:",x)
x = frontier._get()
print("third pop:",x)
x = frontier._get()
print("forth pop:",x)
