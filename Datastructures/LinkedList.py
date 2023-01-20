

class LinkedList:
    

    def __init__(self,data):
        self.data=data
        self.nextNode=None

    def insertNode(self,data):        
        
        if self.nextNode is None :
             self.nextNode = LinkedList(data)
        else:
            iterator = self.nextNode 
            while iterator != None and iterator.nextNode != None:
                iterator = iterator.nextNode
            iterator.nextNode = LinkedList(data)

    def insertHead(self,data):
        secondItem=LinkedList(self.data)
        secondItem.nextNode=self.nextNode
        self.nextNode=secondItem
        self.data=data

    def printLinkedList(self):
        print(self.data)
        iterator=self.nextNode
        while iterator is not None:
            print(iterator.data)
            iterator=iterator.nextNode

    def reverseLinkedList(self):
        previous=None
        current=self
        next=self.nextNode
        while current.nextNode is not None:
            tempHead=current.nextNode
            current.nextNode=previous
            previous=current
            current=tempHead
        current.nextNode=previous
        return current
        

        







