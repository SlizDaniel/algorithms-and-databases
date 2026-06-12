def recoursive_cost(P, i, T, j):
    if i==0:
        return j
    if j==0:
        return i    
    costs = []
    costs.append(1 + recoursive_cost(P, i, T, j-1))
    costs.append(1 + recoursive_cost(P, i-1, T, j))
    change_cost = 0
    if P[i-1]!=T[j-1]:
        change_cost+=1
    costs.append(change_cost + recoursive_cost(P, i-1, T, j-1))
    cost_to_return = min(costs)
    costs = []

    return cost_to_return

def PD_cost (P ,i, T, j):
    rows = len(P)
    cols = len(T)
    D = []
    for _ in range(rows):
        D.append([0 for col in range(cols)])
    for _ in range(len(D[0])):
        D[0][_]=_
    for _ in range (len(D)):
        D[_][0]=_

    Parents = []
    for _ in range(rows):
        Parents.append(['X' for col in range(cols)])
    for _ in range(len(Parents[0])):
        if _!=0:
            Parents[0][_]='I'
    for _ in range (len(Parents)):
        if _!=0:
            Parents[_][0]='D'

    for i in range (1, rows):
        for j in range (1, cols):   
                insert_cost = D[i][j-1] + 1
                remove_cost = D[i-1][j] + 1
                change_cost = D[i-1][j-1] + (P[i]!=T[j])
                min_ = min(insert_cost, remove_cost, change_cost)
                if min_ == change_cost:
                    if P[i]==T[j]:
                        operation = 'M'
                    else:
                        operation = 'R'
                elif min_==remove_cost:
                    operation = 'D'
                else:
                    operation = 'I'
                D[i][j] = min_
                Parents[i][j] = operation
    return D, Parents, D[rows-1][cols-1]

def subsequence(P, i, T, j):
    rows = len(P)
    cols = len(T)
    D = []
    for _ in range(rows):
        D.append([0 for col in range(cols)])
    for _ in range (len(D)):
        D[_][0]=_
    Parents = []
    for _ in range(rows):
        Parents.append(['X' for col in range(cols)])
    for _ in range (len(Parents)):
        if _!=0:
            Parents[_][0]='D'
    for i in range (1, rows):
        for j in range (1, cols):   
                insert_cost = D[i][j-1] + 1
                remove_cost = D[i-1][j] + 1
                change_cost = D[i-1][j-1] + (P[i]!=T[j])
                min_ = min(insert_cost, remove_cost, change_cost)
                if min_ == change_cost:
                    if P[i]==T[j]:
                        operation = 'M'
                    else:
                        operation = 'R'
                elif min_==remove_cost:
                    operation = 'D'
                else:
                    operation = 'I'
                D[i][j] = min_
                Parents[i][j] = operation
    min_value = min(D[rows-1])
    index_to_return = D[rows-1].index(min_value)
    index_to_return-=(len(P)-1)
    return index_to_return, min_value

def longest_cosequence(P,i,T,j):
    rows = len(P)
    cols = len(T)
    D = []
    for _ in range(rows):
        D.append([0 for col in range(cols)])
    for _ in range(len(D[0])):
        D[0][_]=_
    for _ in range (len(D)):
        D[_][0]=_
    Parents = []
    for _ in range(rows):
        Parents.append(['X' for col in range(cols)])
    for _ in range(len(Parents[0])):
        if _!=0:
            Parents[0][_]='I'
    for _ in range (len(Parents)):
        if _!=0:
            Parents[_][0]='D'
    for i in range (1, rows):
        for j in range (1, cols):   
                insert_cost = D[i][j-1] + 1
                remove_cost = D[i-1][j] + 1
                change_cost = D[i-1][j-1] + 10000*(P[i]!=T[j])
                min_ = min(insert_cost, remove_cost, change_cost)
                if min_ == change_cost:
                    if P[i]==T[j]:
                        operation = 'M'
                    else:
                        operation = 'R'
                elif min_==remove_cost:
                    operation = 'D'
                else:
                    operation = 'I'
                D[i][j] = min_
                Parents[i][j] = operation
    coseq_to_return = ''
    rows = len(Parents)-1
    cols = len(Parents[0])-1
    current_string_to_add = Parents[rows][cols]
    while current_string_to_add != 'X':
        match current_string_to_add:
            case 'I':
                cols-=1
            case 'D':
                rows-=1
            case 'M':
                coseq_to_return+=P[rows]
                rows-=1
                cols-=1
            case 'R':
                rows-=1
                cols-=1
        current_string_to_add = Parents[rows][cols]
    return coseq_to_return[::-1]

def path_recreation(Parent: list[list[str]]):
    operations = ''
    rows = len(Parent)-1
    cols = len(Parent[0])-1
    current_string_to_add = Parent[rows][cols]
    while current_string_to_add != 'X':
        operations+=current_string_to_add
        match current_string_to_add:
            case 'I':
                cols-=1
            case 'D':
                rows-=1
            case 'M':
                rows-=1
                cols-=1
            case 'R':
                rows-=1
                cols-=1
        current_string_to_add = Parent[rows][cols]
    return operations[::-1]

def main():
    P = ' kot'
    T = ' pies'
    i = len(P)
    j = len(T)
    print(recoursive_cost(P, i, T, j))
    P = ' biały autobus'
    T = ' czarny autokar'
    i = len(P)
    j = len(T)
    print(PD_cost(P,i,T,j)[2])
    P = ' thou shalt not'
    T = ' you should not' 
    i = len(P)
    j = len(T)      
    print(path_recreation(PD_cost(P,i,T,j)[1]))
    P = ' ban'
    T = ' mokeyssbanana'
    i = len(P)
    j = len(T)
    print(subsequence(P,i,T,j))
    P = ' bin'
    T = ' mokeyssbanana'
    i = len(P)
    j = len(T)
    print(subsequence(P,i,T,j))
    P = ' democrat'
    T = ' republican'
    i = len(P)
    j = len(T)
    print(longest_cosequence(P,i,T,j))
    T = ' 243517698'
    T_int = []
    for ch in T:
        if ch!=' ':
            T_int.append(int(ch))
    P_int = sorted(T_int)
    P=' '
    for i in P_int:
        P+=str(i)
    i = len(P)
    j = len(T)
    print(longest_cosequence(P,i,T,j))


if __name__ == "__main__":
    main()