class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    # Add an element to the end of the list
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
   
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
   
        self.__size += 1 # Increase size
 
    # Same as addLast
    def add(self, e):
        self.addLast(e)
 
 
 
    # Remove the head node and
    #  return the object that is contained in the removed node.
    def removeFirst(self):
        if self.__size == 0:
            return None  # Nothing to delete
        else:
            temp = self.__head  # Keep the first node temporarily
            self.__head = self.__head.next  # Move head to point the next node
            self.__size -= 1  # Reduce size by 1
        if self.__head is None:
            self.__tail = None  # List becomes empty
        return temp.data  # Return the deleted element
 
 
 
    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list.
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
   
            for i in range(1, index):
                previous = previous.next
       
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element
 
    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
   
    # Return the size of the list
    def getSize(self):
        return self.__size