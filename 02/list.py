class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class Llist:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, arg):
        node = ListNode(arg)
        node.next = self.head
        self.head = node

    def append(self, arg):
        node = ListNode(arg)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = node

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        temp.next = None

    def __str__(self):
        if self.head is None:
            return ""
        first = self.head
        str_ = ""
        while(first):
            str_+=f"->{first.data}\n"
            first = first.next
        return str_


    def length(self):
        leng = 0
        if self.head:
            leng+=1
            current = self.head
            while(current.next):
                leng+=1
                current = current.next
        return leng

    def get(self):
        if self.head is not None:
            return self.head.data
        return None
        
def main():
    lista = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]
    uczelnie = Llist()
    for i in range (0, 3):
        uczelnie.append(lista[i])
    for i in range (3, 6):
        uczelnie.add(lista[i])
    print(uczelnie)
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(lista[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

if __name__ == "__main__":
    main()
