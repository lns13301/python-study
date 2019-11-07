class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        if self.left == None:
            if self.right == None:
                return "{}".format(self.data)
            else:
                return "{}, {}".format(self.data, self.right)
        elif self.right == None:
            return "{}, {}".format(self.data, self.left)
        else:
            return "{}, {}, {}".format(self.data, self.left, self.right)

a = Node(4, Node(3, Node(1), Node(2)), Node(5, Node(6), Node(7)))


print(a)
