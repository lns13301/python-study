class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        if self.next != None:
            return "{},{}".format(self.data, self.next)
        else:
            return "{}".format(self.data)
        

def max(lst):
    rest = lst
    mx = lst
    prev = None
    while lst.next != None:
        if mx.data < lst.next.data:
            prev = lst
            mx = lst.next
        lst = lst.next
        
    if prev != None:
        prev.next = mx.next
        mx.next = None

    if mx == rest:
        rest = rest.next
        mx.next = None
        return mx, rest
    else:
        return mx, rest

def addList(lst, node):
    head = node
    if node == None:
        return lst
    while node.next != None:
        node = node.next
    node.next = lst
    return head

def sortList(lst):
    tempLst = None
    while lst != None:
        tuple = max(lst)
        tempLst = addList(tempLst, tuple[0])
        lst = tuple[1]
    return tempLst

lnklst = Node(11, Node(2, Node(15, Node(5, Node(10)))))
print(lnklst)
tuple = max(lnklst)
print(tuple[0])
print(tuple[1])
print(sortList(addList(tuple[1], tuple[0])))

