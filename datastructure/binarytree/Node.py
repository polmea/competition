# A Node class is the sufficient data structure to represent a binary tree.

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left  = n2
n1.right = n3