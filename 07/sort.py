class Element:
    def __init__(self, data, prio):
        self.__data = data
        self.__prio = prio

    def __eq__(self, other):
        if self.__prio == other.__prio:
            return True
        return False

    def __lt__(self, other):
        if self.__prio < other.__prio:
            return True
        return False
    
    def __gt__(self, other):
        if self.__prio > other.__prio:
            return True
        return False
    
    def __le__(self, other):
        if self.__prio<=other.__prio:
            return True
        return False
    
    def __ge__(self, other):
        if self.__prio<=other.__prio:
            return True
        return False
    
    def __repr__(self):
        return f"{self.__prio} : {self.__data}"
    
class Heap:
    def __init__(self, to_sort_tab = None):
        if to_sort_tab == None:
            self.queue = []
            self.size = 0
        else: 
            self.queue = to_sort_tab
            self.size = len(self.queue)
            self.__build_heap()

    def __build_heap(self):
        if self.size < 2:
            return
        else:
            last_parent = self.__parent(self.size-1)
            for i in range (last_parent, -1, -1):
                self.__repair_heap(i)
        return

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
        #self.queue[0] = self.queue[self.size-1]
        self.__change_positions(idx, self.size-1)
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

def swap_sort(list_):
    iterations = len(list_)
    for i in range (0, iterations):
        min_elem = min(list_[i:])
        min_idx = list_.index(min_elem, i)
        if list_[min_idx]<list_[i]:
            list_[min_idx], list_[i] = list_[i], list_[min_idx]
    return list_

def shift_sort(list_):
    for i in range (1, len(list_)):
        to_insert = list_.pop(i)
        j = i - 1
        while j>=0 and to_insert<list_[j]:
            j-=1
        list_.insert(j+1, to_insert)
    return list_

def test1 (to_sort_elements):
    list_ = [ Element(prio, data) for data, prio in  to_sort_elements]
    to_sort_heap = Heap(list_)
    to_sort_heap.print_tab()
    to_sort_heap.print_tree(0,0)
    while(not to_sort_heap.is_empty()):
        to_sort_heap.dequeue()
    output_list_size = len(to_sort_elements)
    to_sort_heap.size = output_list_size
    to_sort_heap.print_tab()
    print("NIESTABILNE")
    list_ = [ Element(prio, data) for data, prio in  to_sort_elements]
    print(swap_sort(list_))
    print("NIESTABILNE")
    list_ = [ Element(prio, data) for data, prio in  to_sort_elements]
    print(shift_sort(list_))
    print("STABILNE")

import random
import time

def test2():
    numbers_list = []
    for i in range (0, 10000):
        numbers_list.append(int(random.random() * 100)) 
    #przez rozebranie
    t_start = time.perf_counter()
    to_sort_list = Heap(numbers_list.copy())
    while(not to_sort_list.is_empty()):
        to_sort_list.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    #sortowanie swap
    t_start = time.perf_counter()
    swap_sort(numbers_list.copy())
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    #sortowanie shift
    t_start = time.perf_counter()
    shift_sort(numbers_list.copy())
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
   

def main(test_number):
    
    data_list_ = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    
    if test_number == 1:
        test1(data_list_)
    elif test_number == 2:
        test2()
    

if __name__ == "__main__":
    test_numbers = [1, 2]
    for i in test_numbers:
        main(i)