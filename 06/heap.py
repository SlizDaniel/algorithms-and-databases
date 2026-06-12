class Element:
    def __init__(self, data, prio):
        self.__data = data
        self.__prio = prio

    def __lt__(self, other):
        if self.__prio < other.__prio:
            return True
        return False
    
    def __gt__(self, other):
        if self.__prio > other.__prio:
            return True
        return False
    
    def __repr__(self):
        return f"{self.__prio} : {self.__data}"
    
class Heap:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def peek(self):
        if self.size == 0:
            return None
        return self.queue[0]
    
    def __left(self, idx):
        return idx*2+1
    
    def __right(self, idx):
        return idx*2+2
    
    def __parent(self, idx):
        return (idx-1)//2
    
    def enqueue(self, elem: Element):
        if self.size == len(self.queue):
            self.queue.append(elem)
        else:
            self.queue[self.size] = elem
        self.size += 1
        idx_elem = self.size - 1
        if idx_elem == 0:
            return
        idx_parent = self.__parent(idx_elem)
        while(idx_elem>0 and elem > self.queue[idx_parent]):
            self.__change_positions(idx_parent, idx_elem)
            idx_elem = idx_parent
            idx_parent = self.__parent(idx_parent)
        return
    
    def __change_positions (self, idx1, idx2):
        elem = self.queue[idx2]
        to_copy = self.queue[idx1]
        self.queue[idx1] = elem
        self.queue[idx2] = to_copy
        return

    def dequeue(self):
        if self.is_empty():
            return None
        to_return = self.queue[0]
        idx = 0
        self.queue[0] = self.queue[self.size-1]
        self.size -= 1
        if (not self.is_empty()):
            self.__repair_heap(idx)
        return to_return
            
    def __repair_heap (self, idx):
        current_idx = idx
        repaired = False
        while(not repaired):
            left_child = self.__left(current_idx)
            right_child = self.__right(current_idx)
            largest_idx = current_idx
            if left_child < self.size and self.queue[left_child]>self.queue[largest_idx]:
                largest_idx = left_child
            if right_child < self.size and self.queue[right_child]>self.queue[largest_idx]:
                largest_idx = right_child
            if largest_idx != current_idx:
                self.__change_positions(current_idx, largest_idx)
                current_idx = largest_idx
            else:
                repaired = True

    def print_tab(self):
        print ('{', end=' ')
        print(*self.queue[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.__right(idx), lvl+1)
            print(2*lvl*'  ', self.queue[idx] if self.queue[idx] else None)           
            self.print_tree(self.__left(idx), lvl+1)

def main():
    heap = Heap()
    string = "GRYMOTYLA"
    prios = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    for i in range (0, len(prios)):
        elem = Element(string[i], prios[i])
        heap.enqueue(elem)
    heap.print_tree(0,0)
    heap.print_tab()
    curr_max = heap.dequeue()
    print(heap.peek())
    heap.print_tab()
    print(curr_max)
    while(not heap.is_empty()):
        print(heap.dequeue())
    heap.print_tab()
    return


if __name__ == "__main__":
    main()