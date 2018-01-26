# class Node(object):
#     def __init__(self, value, nextnode=None):
#         self.value = value
#         self._nextnode = nextnode

#     def append(self, n):
#         if not isinstance(n, Node):
#             n = Node(n)
#         self._nextnode, n = n, self._nextnode
#         self._nextnode._nextnode = n

# n=Node(1)
# print(n.value)
# n.append(2)
# print(n._nextnode.value)
# print(n._nextnode._nextnode.value)

class Node(object):
    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode

    def append(self, nextvalue):
        if not isinstance(nextvalue, Node):
            n = Node(nextvalue)
            self._nextnode=n
        else:
        	self._nextnode=nextvalue

n1=Node(1)
n2=Node(2)
n1.append(n2)
print(n1._nextnode.value)
