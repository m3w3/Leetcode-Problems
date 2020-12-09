class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d_to_point, p_distances = {}, []
        for point in points:
            distance = point[0]**2 + point[1]**2
            if distance not in d_to_point:
                d_to_point[distance] = [point]
                p_distances.append(distance)
            else: 
                d_to_point[distance].append(point)
        
        # now retrieve the top K distances
        p_distances.sort()
        return_l = []
        for distance in p_distances:
            curr_points_in_distance = len(d_to_point[distance])
            if curr_points_in_distance >= K:
                return return_l + d_to_point[distance][:K]
            else:
                return_l += d_to_point[distance]
                K -= curr_points_in_distance
        return return_l
