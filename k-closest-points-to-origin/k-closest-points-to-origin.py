class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d_to_point, p_distances = {}, []
        for point in points:
            distance = distance_squared(point)
            if distance not in d_to_point:
                d_to_point[distance] = [point]
                p_distances.append(distance)
            else: 
                d_to_point[distance].append(point)
        
        # now retrieve the top K distances
        p_distances.sort()
        return_l = []
        for distance in p_distances:
            print(distance)
            if len(d_to_point[distance]) >= K:
                return return_l + d_to_point[distance][:K]
            else:
                return_l += d_to_point[distance]
                K -= len(d_to_point[distance])
        return return_l
​
    
def distance_squared(p) -> int:
    return p[0]**2 + p[1]**2
