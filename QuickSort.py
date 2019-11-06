class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        if self.next != None:
            return "{},{}".format(self.data, self.next)
        else:
            return "{}".format(self.data)

def quickSort(lst):
    lowList = None
    highList = None
    if lst == None:
        return lst
    pivot = lst
    lst = lst.next
    while lst != None:
        if pivot.data >= lst.data:
            lowList = addList(lowList, Node(lst.data))
        else:
            highList = addList(highList, Node(lst.data))
        lst = lst.next
    return addList(addList(quickSort(lowList), quickSort(pivot)), quickSort(highList))

def addList(lst, node):
    head = lst
    if lst == None:
        return node
    if node == None:
        return lst
    while lst.next != None:
        lst = lst.next
    lst.next = node
    return head

lnklst = Node(11, Node(2, Node(15, Node(5, Node(10)))))
print(quickSort(lnklst))
