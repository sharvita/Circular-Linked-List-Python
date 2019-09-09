# this is the node class which has data and next
class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None
# this is the actual circular linked list class which is made of Nodes
class CircularLinkedList:

    size = 0 #
    # size of the list

    # constructor
    def __init__(self):
        self.head = None
        self.tail = None

    #this inserts the node at the very front of the list
    def insertAtFront(self, node):


        if self.head is None: # head is null
            node.next = self.head
            self.head = node
            self.tail = node
            self.tail.next = self.head

        else: #if head is not null
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1 #size increases

    #this is used to insert at the very bcak of th lisr
    def insertAtBack(self, node):

        # Case when list is empty
        if self.head is None:
            self.insertAtFront(node)

        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
            self.size += 1

    #this function does not fully work but should allow the user to insert at a certain index
    def insertAt(self,node, index):

        if self.head is None or index == 0 :
            self.insertAtFront(node)
        elif index == self.size :
            self.insertAtBack(node)
        else :
            current_node = Node(None)
            if 0 < index < self.size:
                current_node = self.head.next
                position = 0

            while position < index - 1:
                position += 1
                current_node = current_node.next

            node = Node(node.data)
            current_node.next = node
            self.shiftToleft()

    #this shifts the list to the left  and is used when a certain node is inserted at a index
    def shiftToleft(self):
        temp = self.head
        if self.head is not None:
            while (True):
                if (temp.next == self.tail):
                    break
                temp = temp.next
            self.head = self.tail
            self.tail = temp

    #this function prints the list
    def print(self):
        print("The list contains : ")
        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break

#Creating nodes to put into the list
list = CircularLinkedList()
for x in range(5):
    newNode = Node(x)
    list.insertAtBack(newNode)


node = Node(10)
list.insertAtFront(node)
list.shiftToleft()
#list.insertAt(node,2)
print("Following is the list ")
list.print()
print("Size of list is %d " % list.size)


