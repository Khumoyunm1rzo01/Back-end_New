# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val 
#         self.next = next

# a4 = Node(4)
# a3 = Node(3, a4)
# a2 = Node(2, a3)
# a1 = Node(1, a2)

# curr = a1
# while curr != None:
#     print(curr)

# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def append(self, val):
#         node = Node(val)
#         node.next = self.head
#         self.head = node
    
#     def print_list(self):
#         curr = self.head
#         while curr != None:
#             print(curr.val)
#             curr = curr.next

# mylist = LinkedList()
# mylist.append(5)
# mylist.append(4)
# mylist.append(3)
# mylist.append(2)
# mylist.append(1)
# mylist.print_list()
# print("finished")