# def print_items(n):
#     for i in range(n):
    
#         for j in range(n):
#             print(i,j)
    
#     for k in range(n):
#         print(k)


# print_items(10)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp



my_linked_list = LinkedList(2)
my_linked_list.append(3)

# my_linked_list.print_list()

# it will return my second node (last one in the linked list)
# print(my_linked_list.pop())

# it will return my first node (actually last)
# print(my_linked_list.pop())

# it will return None
# print(my_linked_list.pop())

my_linked_list.prepend(1)
# my_linked_list.print_list()

print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())

