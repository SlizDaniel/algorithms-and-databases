class CyclicList:
    def __init__(self, idxIN=0, idxOUT=0):
        self._idxIN = idxIN
        self._idxOUT = idxOUT
        self._cyclicList = [None for i in range (5)]

    def is_empty(self):
        if self._idxIN == self._idxOUT:
            return True
        return False
    
    def peek(self):
        if self.is_empty():
            return None
        return self._cyclicList[self._idxOUT]
    
    def dequeue(self):
        if self.is_empty():
            return None
        idx_copy = self._idxOUT
        toReturn = self._cyclicList[idx_copy]
        if self._idxOUT == len(self._cyclicList) - 1:
            self._idxOUT = 0
        else:
            self._idxOUT += 1
        self._cyclicList[idx_copy] = None
        return toReturn

    def enqueue(self, data):
        self._cyclicList[self._idxIN] = data
        self._idxIN += 1
        if self._idxIN == len(self._cyclicList):
            self._idxIN = 0
        if self._idxIN == self._idxOUT:
            newList = [None for i in range (len(self._cyclicList)*2)]
            copied_elements = 0
            while(copied_elements < len(self._cyclicList)):
                currentElement = self._cyclicList[self._idxOUT]
                if currentElement!=None:
                    newList[len(self._cyclicList) + copied_elements] = currentElement
                    copied_elements += 1
                    self._idxOUT+=1
                    if self._idxOUT == len(self._cyclicList):
                        self._idxOUT = 0
            self._idxIN = 0
            self._idxOUT = len(self._cyclicList)
            self._cyclicList = newList
        return self._cyclicList
        
    def __str__(self):
        output = []
        temporary = self._idxOUT     
        while(self._cyclicList[temporary] != None and temporary != self._idxIN):
            output.append(self._cyclicList[temporary])
            temporary += 1
            if(temporary == len(self._cyclicList)):
                temporary = 0
        return f"{output}"       
    
    def listState(self):
        return f"{self._cyclicList}"

def main():
    newQueue = CyclicList()
    for i in range (1, 5):
        newQueue.enqueue(i)
    print(newQueue.dequeue())
    print(newQueue.peek())
    print(newQueue)
    for i in range (5, 9):
        newQueue.enqueue(i)
    print(newQueue.listState())
    while(newQueue.is_empty() == False):
        print(newQueue.dequeue())
    print(newQueue)

if __name__ == "__main__":
    main()
            