class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next
# Beginning of exercise

    def insert(self, head, data):
        node = Node(data)
        if head is None:
            head = node
        elif head.next is None:
            head.next = node
        else:
            head = head.next
            while head.next is not None:
                head = head.next
            head.next = node



# End of exercise

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
