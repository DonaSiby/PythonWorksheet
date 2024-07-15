# Given a linkedlist, determine if it has a cycle in it.

class Solution(object):
  def hasCycle(self,head):
    if head == None:
      return False
    else:
      fast = head
      slow = head

      while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
          break

      if fast == None or fast.next == None:
        return False
      elif fast == slow:
        return True
      return False


"""
# Python program to detect loop in the linked list

# Node class


class Node:

    # Constructor to initialize the node object
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return 1
        return 0


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head
if(llist.detectLoop()):
    print("Loop Found")
else:
    print("No Loop")

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

"""
