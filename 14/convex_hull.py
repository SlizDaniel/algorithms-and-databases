import math

def jarvis_algorithm(points:list, flag: str):
    min_x = float('inf')
    min_y = float('inf')
    for x,y in points:
        if x < min_x:
            min_x = x
            min_y = y
        elif x == min_x:
            if y<min_y:
                min_x = x
                min_y = y
            else:
                continue
    edge_points = []
    current_point = min_x, min_y
    starting_point = current_point
    edge_points.append(current_point)
    returned_to_start = False
    current_point_idx = points.index((min_x,min_y))
    next_point = points[(current_point_idx+1)%len(points)]
    while(not(returned_to_start)):
        for point in points:
            if point!=next_point and point!=current_point:
                direction = (next_point[1]-current_point[1])*(point[0]-next_point[0])-(point[1]-next_point[1])*(next_point[0]-current_point[0])
                 # (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)
                if direction>0:
                    next_point = point
                if flag == 'true':
                    if direction == 0:
                        distance_next = math.sqrt((next_point[0]-current_point[0])**2 + (next_point[1]-current_point[1])**2)
                        distance_point = math.sqrt((point[0]-current_point[0])**2 + (point[1]-current_point[1])**2)
                        
                        if distance_point>distance_next:
                            next_point = point

        edge_points.append(next_point)
        current_point = next_point
        current_point_idx = points.index(current_point)
        next_point = points[(current_point_idx+1)%len(points)]
            
        if (current_point == starting_point):
            returned_to_start = True

    return edge_points

def graham_algorithm(points:list):
    min_x = 1000
    min_y = 1000
    for x,y in points:
        if y<min_y:
            min_y = y
            min_x = x
        elif y==min_y:
            if x<min_x:
                min_y = y
                min_x = x
        # idx = points.index((min_x, min_y))
    P0 = ((min_x, min_y))
    P0_idx = points.index(P0)
    points[0],points[P0_idx] = points[P0_idx], points[0]
    for i in range (1, len(points)):
        for j in range (1, len(points)-1):
            point = points[j]
            next_point = points[(j+1)%len(points)]
        # (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)
            angle = (point[1]-P0[1])*(next_point[0]-point[0])-(next_point[1]-point[1])*(point[0]-P0[0])
            in_order = False
            if angle < 0:
                in_order = True
            elif angle == 0:
                distance_point = math.sqrt((point[0]-P0[0])**2 + (point[1]-P0[1])**2)
                distance_next_point = math.sqrt((next_point[0]-P0[0])**2 + (next_point[1]-P0[1])**2)
                if distance_point>distance_next_point:
                    in_order = False
            if (not in_order):
                points[j], points[j+1] = points[j+1], points[j]
    
    deleted = False
    i=1
    while not deleted:
        point = points[i]
        next_point = points[i+1]
        angle = (point[1]-P0[1])*(next_point[0]-point[0])-(next_point[1]-point[1])*(point[0]-P0[0])
        if angle == 0:
            points.pop(i)
        else:
            i+=1
        if i == len(points)-1:
            deleted = True
    
    if len(points)<3:
        print("edge impossible")
        return None

    edge = points[:3]

    for i in range(3, len(points)):
        p3 = points[i]
        while len(edge) >= 2:
            p1 = edge[-2]
            p2 = edge[-1]
            angle = (p2[1]-p1[1])*(p3[0]-p2[0])-(p3[1]-p2[1])*(p2[0]-p1[0])
            if angle >= 0:
                edge.pop()
            else:
                break
        edge.append(p3)

    return edge


def main():
    list1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    list2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    list3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    list4 = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    print(jarvis_algorithm(list3, 'true'))
    print(jarvis_algorithm(list3, 'false'))
    print(graham_algorithm(list4))

if __name__ == "__main__":
    main()