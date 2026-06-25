class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
       self.head = ListNode(-1)
       self.tail=self.head
    
    def get(self, index: int) -> int:
       if index <0:
        return -1
       i=0
       curr = self.head.next
       while curr and i<index:
         i+=1
         curr = curr.next
       if curr:
        return curr.val
       return -1
    
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next=node
        if self.tail == self.head:  # list was empty before insert
         self.tail = node
        
    def insertTail(self, val: int) -> None:
        self.tail.next= ListNode(val)
        self.tail =self.tail.next

    def remove(self, index: int) -> bool:
     if index < 0:
        return False

     prev = self.head
     i = 0

    # stop at the node BEFORE the one to remove
     while prev.next and i < index:
        prev = prev.next
        i += 1

     if prev.next is None or i != index:
        return False

     removed = prev.next
     prev.next = removed.next

    # update tail if needed
     if removed == self.tail:
        self.tail = prev

     return True


    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next  # skip dummy head
        while curr:
          values.append(curr.val)
          curr = curr.next
        return values
        
