from typing import List, Optional

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"

class Deleted:
    def __repr__(self):
        return "None"

class HashTable:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.c1 = c1
        self.c2 = c2
        self.size = size
        self.tab_ : List[Optional[Element|Deleted]]= [None for _ in range (self.size)]

    def transform_function(self, key):
        if isinstance(key, str):
            sum_key=0
            for ch in key:
                sum_key+=ord(ch)
            return sum_key%self.size
        return key%self.size


    def search (self, key):
        idx1 = self.transform_function(key)
        elem = self.tab_[idx1]
        if elem is not None or not isinstance(elem, Deleted):      
            if isinstance(elem, Element) and elem.key == key:
                return elem.value
            maxIterations = self.size
            count = 0
            found = False
            while(found == False):
                if count < maxIterations:
                    idx = (idx1 + self.c1 * count + self.c2 * count**2)%self.size
                    if(self.tab_[idx] is None):
                        return None
                    if isinstance(self.tab_[idx], Element) and self.tab_[idx].key == key:
                        return self.tab_[idx].value
                    else:
                        count+=1
                else:
                    found = True
        return None
    
    def insert(self, key, value):
        idx1 = self.transform_function(key)
        current = self.tab_[idx1]
        if(current is None):
            current = Element(key, value)
            self.tab_[idx1] = current
            return
        if(isinstance(current, Element) and current.key == key):
            current.value = value
            return
        solved = False
        count = 0
        while(solved==False and self.size>count):
            new_idx = (idx1 + self.c1*count + self.c2*count**2)%self.size
            current = self.tab_[new_idx]
            if current is None or isinstance(current, Deleted):
                current = Element(key, value)
                self.tab_[new_idx] = current
                solved = True
                return
            if current.key == key:
                current.value = value
                return
            count+=1
        raise Exception("Brak miejsca")
    
    def remove(self, key):
        idx1 = self.transform_function(key)
        removed = False
        count = 0
        while(removed == False and count<self.size):
            new_idx = (idx1 + self.c1*count + self.c2*count**2)%self.size
            current = self.tab_[new_idx]
            if current is None:
                raise Exception("Brak danej o podanym kluczu")
            if(isinstance(current, Element) and current.key == key):
                self.tab_[new_idx] = Deleted()
                removed = True
                return
        raise Exception("Brak danej o podanym kluczu")
    
    def __str__(self):
        output = []
        for elem in self.tab_:
            if isinstance(elem, Element):
                output.append(f"{elem.key}:{elem.value}")
            else: output.append("None")
        return "{" + ", ".join(output) + "}"
    
def test1(size, c1, c2):
    tab = HashTable(size, c1, c2)
    for i in range (0, 15):
        key = i + 1
        if key == 6:
            key = 18
        if key == 7:
            key = 31
        try:
            tab.insert(key, chr(65 + i))
        except Exception as message:
            print(message)
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5, 'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    tab.insert('test', 'W')
    print(tab)

def test2(size, c1, c2):
    tab = HashTable(size, c1, c2)
    for i in range (0, 15):
        key = (i + 1) * 13 
        try:
            tab.insert(key, chr(65 + i))
        except Exception as message:
            print(message)
    print(tab)

def main():
    test1(13, 1, 0)
    test2(13, 1, 0)
    test2(13, 0, 1)
    test1(13, 0, 1)

    return
if __name__ == "__main__":
    main()
