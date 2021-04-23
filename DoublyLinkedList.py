class Node:
    def __init__(self, data):
        self.pNext = None
        self.pPrev = None
        self.data = data

class LLIST(Node):
    def __init__(self):
        self.pHead = None
        self.pTail = None
        self.count = 0
    
    def getCount(self):
        return self.count

    def pushBack(self, data):
        pNode = Node(data)
        if (self.pTail == None):
            self.pHead = self.pTail = pNode
        else:
            self.pTail.pNext = pNode
        pNode.pPrev = self.pTail
        self.pTail = pNode
        self.count += 1
    
    def pushFront(self, data):
        pNode = Node(data)
        if (self.pHead == None):
            self.pHead = self.pTail = pNode
        else:
            self.pHead.pPrev = pNode
        pNode.pNext = self.pHead
        self.pHead = pNode
        self.count += 1
    
    def insertItemAfterNode(self, pNode, data):
        pNewNode = Node(data)

        # x1 <-> x2 -> O <-> x3 <-> x4
        if pNode.pNext != None:
            pNode.pNext.pPrev = pNewNode
        else:
            self.pTail = pNewNode
        pNewNode.pNext = pNode.pNext
        pNewNode.pPrev = pNode
        pNode.pNext = pNewNode

        self.count += 1

        return pNewNode
    
    def insertItemBeforeNode(self, pNode, data):
        pNewNode = Node(data)

        # x1 <-> O x2 <-> x3 <-> x4 

        if pNode.pPrev != None:
            pNode.pPrev.pNext = pNewNode
        else:
            self.pHead = pNewNode
        pNewNode.pNext = pNode
        pNewNode.pPrev = pNode.pPrev
        pNode.pPrev = pNewNode

        self.count += 1

        return pNewNode
    
    def insertItemIndex(self, index, data):
       
        pTemp = self.pHead
        if (index == 0):
            self.pushFront(data)
        
        for i in range(0, index - 1):
            pTemp = pTemp.pNext
        
        self.insertItemAfterNode(pTemp, data)

    def popBack(self):

        # x1 <-> x2 <-> x3 <-> x4

        val = self.pTail.data

        if self.count == 0:
            print('Empty List!')
        else:
            self.pTail = self.pTail.pPrev
            self.pTail.pNext = None

        self.count -= 1
        return val

    
    def popFront(self):
        val = self.pHead.data

        if self.count == 0:
            print('Empty List!')
        else:
            self.pHead = self.pHead.pNext
            self.pHead.pPrev = None

        self.count -= 1

        return val


    def display(self):
        pTemp = self.pHead
        if self.count == 0:
            print('Empty List!')
        else:
            while (pTemp != None):
                print(pTemp.data, end=' ')
                pTemp = pTemp.pNext
        print()

if __name__ == '__main__':
    
    hList = LLIST()
    hList.pushBack(15)
    hList.pushBack(23)
    hList.display()

    hList.pushFront(18)
    hList.display()
    hList.pushFront(97)
    hList.display()