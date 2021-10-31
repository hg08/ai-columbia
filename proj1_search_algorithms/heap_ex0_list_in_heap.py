import queue as Q

frontier = Q.PriorityQueue()

l1 = [0,2,'like']
l2 = [0,1,4]
l3 = [0,2,'you']
l4 = [2,3,4]

frontier._put(l3)
frontier._put(l4)
frontier._put(l1)
frontier._put(l2)

x = frontier._get()
print("first pop:",x)
x = frontier._get()
print("second pop:",x)
x = frontier._get()
print("third pop:",x)
x = frontier._get()
print("forth pop:",x)
