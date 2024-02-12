class Node:
    def __init__(self,val,nextNode=None):
        self.nextNode=nextNode
        self.val=val
class MyLinkedList:

    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
        current=self.head
        if current==None :
            return -1 
        for i in range(index):
            if current.nextNode==None:
                return -1
            current=current.nextNode
        return current.val

    def addAtHead(self, val: int) -> None:
        newNode=Node(val,self.head)
        self.head=newNode
            
    def addAtTail(self, val: int) -> None:
        current= self.head
        if self.head==None:
            self.head=Node(val)
            return 
        while current.nextNode !=None:
            current=current.nextNode
        current.nextNode=Node(val) 

    def addAtIndex(self, index: int, val: int) -> None:
        current=self.head
        if index==0:
            newNode=Node(val,self.head)
            self.head=newNode
            return 
        for i in range(index):
            if current==None:
                return
            prev=current
            current=current.nextNode if current.nextNode else None

        prev.nextNode=Node(val,current)
        
    def deleteAtIndex(self, index: int) -> None:
        current=self.head
        if index==0:
            temp=self.head
            self.head=self.head.nextNode if self.head.nextNode else None
            return 
        for i in range(index):
            if current.nextNode==None:
                return
            prev=current
            current=current.nextNode
        prev.nextNode=current.nextNode if current.nextNode else None
    
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)