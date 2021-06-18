import queue as Q

def calc_distance(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def create_heuristic_dictionary(intersections, goal):
    heuristic_distances = {}
    goal_x = intersections[goal][0]
    goal_y = intersections[goal][1]
    for i, intersection in intersections.items():
        x = intersection[0]
        y = intersection[1]
        dist = calc_distance(x, goal_x, y, goal_y)
        heuristic_distances[i] = dist
    return heuristic_distances


def shortest_path(M, start, goal):
    shortest_path = None
    curr_path = [start]
    seen = set([])
    if start == goal:
        return curr_path
    roads = M.roads
    intersections = M.intersections
    heuristic_distances = create_heuristic_dictionary(intersections, goal)
    q = Q.PriorityQueue()
    q.put((0, 0, start, curr_path))
    while not q.empty():
        next_node = q.get()
        curr_dist = next_node[0]
        curr_h_dist = next_node[1]
        curr_number = next_node[2]
        curr_path = next_node[3]
        seen.add(curr_number)
        for road in roads[curr_number]:
            x1 = intersections[curr_number][0]
            y1 = intersections[curr_number][1]
            x2 = intersections[road][0]
            y2 = intersections[road][1]
            dist = calc_distance(x1, x2, y1, y2)
            h_dist = heuristic_distances[road]
            if road != goal:
                if road not in seen:
                    q.put((curr_dist+dist, curr_dist+dist+h_dist, road, curr_path + [road]))
            else:
                if not shortest_path:
                    shortest_path = (curr_dist + dist, curr_path + [road])
                else:
                    if shortest_path[0] > curr_dist + dist:
                        shortest_path = (curr_dist + dist, curr_path + [road])
        
    return shortest_path[1]