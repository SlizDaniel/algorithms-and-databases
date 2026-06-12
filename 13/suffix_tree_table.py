# drzewo wyswietlone w postaci slownika slownikow, gdzie mamy id wezla -> 
# wezly do ktorych mozemy przejsc z tego wezla i ich id
class SuffixTree:
    def __init__(self, T:str) -> None:
        self.root = 0
        self.next_node_id = 1
        self.nodes = {self.root: {}} #list of childrens for each node
        self.indexes = {self.root: []}
        self.__build_tree(T)

    def __build_tree(self, T):
        sufixes_tab = find_suffixes(T)
        for sufix in sufixes_tab:
            current_node=self.root
            self.indexes[current_node].append(sufixes_tab.index(sufix))
            for ch in sufix:
                if ch not in self.nodes[current_node]:
                    node_to_add_id = self.next_node_id
                    self.next_node_id+=1
                    self.nodes[node_to_add_id] = {}
                    self.indexes[node_to_add_id] = []
                    self.nodes[current_node][ch] = node_to_add_id
                current_node = self.nodes[current_node][ch]
                self.indexes[current_node].append(sufixes_tab.index(sufix))

    def find_pattern(self, P:str):
        current_node = self.root
        for ch in P:
            if ch in self.nodes[current_node]:
                current_node = self.nodes[current_node][ch]
            else:
                return False
        return True
    
    def __str__(self) -> str:
        return f"{self.nodes}"

class SuffixTable:
    def __init__(self, T) -> None:
        suffix_list = find_suffixes(T)
        self.suffix_table = []
        self.suffix_list = []
        self.__build_table(suffix_list)

    def __build_table(self, suffix_list):
        for i in range (len(suffix_list)):
            self.suffix_table.append(i)
        self.__sort_suffix_table(suffix_list)

    def __sort_suffix_table(self, suffix_list):
        for i in range(0, len(suffix_list)):
            for j in range (0,len(suffix_list)-1):
                if suffix_list[j]>suffix_list[j+1]:
                    suffix_list[j],suffix_list[j+1]=suffix_list[j+1],suffix_list[j]
                    self.suffix_table[j],self.suffix_table[j+1]=self.suffix_table[j+1],self.suffix_table[j]
        self.suffix_list = suffix_list


    def find_pattern(self, Pattern):
        left = 0
        right = len(self.suffix_table)-1
        while left<=right:
            middle = (left+right)//2
            current_idx = self.suffix_table[middle]
            current_suffix = self.suffix_list[middle]
            current_suffix = current_suffix[:len(Pattern)]
            if current_suffix==Pattern:
                return current_idx
            elif current_suffix>Pattern:
                right = middle-1
            else:
                left = middle+1
        return False

    def __str__(self) -> str:
        return f'{self.suffix_table}'
    
def find_suffixes(T:str):
    suffixes_tab = []
    for i in range(len(T)):
        suffixes_tab.append(T[i:]+'$')
    suffixes_tab.append('$')
    return suffixes_tab

def main():
    T = 'banana'
    Tree = SuffixTree(T)
    P1 = 'na'
    P2 = 'ana'
    P3 = 'nana'
    P4 = 'ananas'
    print(Tree.find_pattern(P1))
    print(Tree.find_pattern(P2))
    print(Tree.find_pattern(P3))
    print(Tree.find_pattern(P4))

    Table = SuffixTable(T)
    print(Table)
    print(Table.find_pattern(P1))
    print(Table.find_pattern(P2))
    print(Table.find_pattern(P3))
    print(Table.find_pattern(P4))

    return

if __name__ == "__main__":
    main()