from typing import Any


class Node:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class Bst:
    def __init__(self, root = None):
        self.root = root

    def insert(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
            return
        if key == self.root.key:
            self.root.value = value
            return
        if key>self.root.key:
            if self.root.right == None:
                self.root.right = Node(key, value)
                return
            self.__find_none_root(key, value, self.root.right)
            return
        if key<self.root.key:
            if self.root.left == None:
                self.root.left = Node(key, value)
                return
            self.__find_none_root(key, value, self.root.left)
            return
        
    def __find_none_root(self, key, value, current):
        if current.key == key:
            current.value = value
            return
        if current.key>key:
            if current.left == None:
                current.left = Node(key, value)
                return
            else:
                self.__find_none_root(key, value, current.left)
        if current.key<key:
            if current.right == None:
                current.right = Node(key,value)
                return
            else:
                self.__find_none_root(key, value, current.right)
    
    def search(self, key):
        current = self.root
        while current != None:
            if current == None:
                return None
            if current.key == key:
                return current.value
            elif key>current.key:
                current = current.right
            elif key<current.key:
                current = current.left

    def height(self):
        self.height_ = 0
        if self.root == None:
            return -1
        if self.root.left == None and self.root.right == None:
            return self.height_
        else:
            return self.__recoursive_height(self.root, self.height_)
    

    def __recoursive_height(self, root, current_count):
        right_path = current_count
        left_path = current_count
        current_root = root
        if root.left != None:
            left_path = self.__recoursive_height(current_root.left, current_count+1)
        if root.right != None:
            right_path = self.__recoursive_height(current_root.right, current_count+1)
        return self.__path_decider(left_path, right_path)

    def __path_decider(self, left_path, right_path):
        if left_path>right_path:
            return left_path
        return right_path
    
    def delete(self, key):
        if self.root == None:
            return
        tupl_ = self.__search_elem_to_delete(key)
        if(tupl_ is None):
            return
        current, prev_, side = tupl_
        if current.right == None and current.left == None:
            if prev_ is None:
                self.root = None
            elif side == 'left':
                prev_.left = None
            elif side == 'right':
                prev_.right = None
            return
        if current.left is None or current.right is None:
            if current.left:
                child = current.left
            elif current.right:
                child = current.right
            if prev_ is None:
                self.root = child
            elif side == 'left':
                prev_.left = child
                current = None
            elif side == 'right':
                prev_.right = child
                current = None
            return
        #case 2 child to finish
        next_ = current.right
        parent = current
        next_found = False
        count=0
        while(not next_found):
            prev_ = next_
            cur_ = prev_.left
            if cur_ is None:
                next_found = True
            if count == 1:
                parent = current.right
            if count>1:
                parent = parent.left
            count+=1
            next_ = next_.left
        current.key = prev_.key
        current.value = prev_.value
        if parent == current:
            parent.right = prev_.right
        else:
            parent.left = prev_.right
        return

    def __search_elem_to_delete(self, key):
        current = self.root
        prev_ = None
        side = None
        while current != None:
            if current.key == key:
                return current, prev_, side
            elif key>current.key:
                prev_ = current
                current = current.right
                side = "right"
            elif key<current.key:
                prev_ = current
                current = current.left
                side = "left"
        return None
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

    def print_as_list(self):
        output = self.__tree_in_order(self.root)
        print(f"{output}")

    def __tree_in_order(self, current):
        if current is None:
            return ""
        
        output_left = self.__tree_in_order(current.left)
        output_current = f"{current.key} {current.value},"
        output_right = self.__tree_in_order(current.right)

        return output_left + output_current + output_right
    

def main():
    my_bst = Bst()
    to_add = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, value in to_add.items():
        my_bst.insert(key, value)
    my_bst.print_tree()
    my_bst.print_as_list()
    print(my_bst.search(24))
    my_bst.insert(20, "AA")
    my_bst.insert(6, "M")
    my_bst.delete(62)
    my_bst.insert(59,"N")
    my_bst.insert(100,"P")
    my_bst.delete(8)
    my_bst.delete(15)
    my_bst.insert(55, "R")
    my_bst.delete(50)
    my_bst.delete(5)
    my_bst.delete(24)
    print(my_bst.height())
    my_bst.print_as_list()
    my_bst.print_tree()


if __name__ == "__main__":
    main()