import math
import time 


def recoursive_triangulation(points, main_function = True):
    t_start = time.perf_counter()
    if len(points)<3:
        return 0
    i = points[0]
    j = points[-1]
    initial_cost = calculate_length(i, j)
    min_cost = float('inf')
    for idx in range(1, len(points)-1):
        k=points[idx]
        cost = initial_cost + calculate_length(k,i) + calculate_length(k,j)
        cost += recoursive_triangulation(points[:idx+1], False)
        cost+=recoursive_triangulation(points[idx:],False)
        if cost<min_cost:
            min_cost = cost
    if main_function==True:
        t_stop = time.perf_counter()
        t = t_stop-t_start
        print("Czas wersji rekurencyjnej: ",t)
    return min_cost

def dynamic_triangulation(points):
    t_start = time.perf_counter()
    dp_table = [[0.0 for _ in range(len(points))] for _ in range (len(points))]
    for Lengths in range(3, len(points)+1):
        for i in range (len(points)-Lengths+1):
            j = i+Lengths-1
            min_cost = float('inf')
            for k in range(i+1, j):
                cost = calculate_length(points[i],points[j])+calculate_length(points[i],points[k])+calculate_length(points[k],points[j])
                cost+=dp_table[i][k] + dp_table[k][j]
                if cost<min_cost:
                    min_cost = cost
            dp_table[i][j]=min_cost
    t_stop = time.perf_counter()
    t = t_stop-t_start
    print("Czas wersji dynamicznej: ",t)
    return dp_table[0][len(points)-1]

def calculate_length(point1, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def main():
    points_set1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    points_set2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]
    print(recoursive_triangulation(points_set1))
    print(recoursive_triangulation(points_set2))
    print(dynamic_triangulation(points_set1))
    print(dynamic_triangulation(points_set2))
    
    return

if __name__ == "__main__":
    main()